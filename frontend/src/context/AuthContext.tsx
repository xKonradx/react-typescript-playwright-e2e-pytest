import React, { createContext, useContext, useState, useRef } from "react";
import usersData from "../data/users.json";

export type UserRole = "admin" | "user";
export interface User {
  username: string;
  role: UserRole;
}

interface AuthContextType {
  user: User | null;
  login: (username: string, password: string) => boolean;
  logout: () => void;
  register: (username: string, password: string) => string | true;
  changePassword: (oldPass: string, newPass: string, repeat: string) => string | true;
  generateCSRFToken: () => string;
  validateCSRFToken: (token: string) => boolean;
  isRateLimited: (username: string) => boolean;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

function getAllUsers() {
  const local = localStorage.getItem("users");
  if (local) return JSON.parse(local);
  return usersData;
}

function saveUsers(users: any[]) {
  localStorage.setItem("users", JSON.stringify(users));
}

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({
  children,
}) => {
  const [user, setUser] = useState<User | null>(() => {
    const local = localStorage.getItem("user");
    return local ? JSON.parse(local) : null;
  });

  const loginAttempts = useRef<{ [key: string]: { count: number; lastAttempt: number } }>({});
  const csrfTokens = useRef<Set<string>>(new Set());

  // Enhanced input validation and sanitization
  const sanitizeInput = (input: string): string => {
    // Remove dangerous characters and patterns
    return input
      .replace(/[<>\"'&]/g, '')
      .replace(/javascript:/gi, '')
      .replace(/data:text\/html/gi, '')
      .replace(/on\w+\s*=/gi, '')
      .replace(/';?\s*drop\s+table/gi, '')
      .replace(/union\s+select/gi, '')
      .replace(/insert\s+into/gi, '')
      .replace(/delete\s+from/gi, '')
      .replace(/update\s+set/gi, '')
      .replace(/<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi, '');
  };

  const validateInput = (input: string): boolean => {
    const dangerousPatterns = [
      /<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi,
      /javascript:/gi,
      /data:text\/html/gi,
      /on\w+\s*=/gi,
      /';?\s*drop\s+table/gi,
      /union\s+select/gi,
      /insert\s+into/gi,
      /delete\s+from/gi,
      /update\s+set/gi,
      /<iframe/gi,
      /<object/gi,
      /<embed/gi,
      /<form/gi,
      /<input/gi,
      /<textarea/gi,
      /<select/gi,
      /<button/gi,
      /<link/gi,
      /<meta/gi,
      /<style/gi
    ];
    
    return !dangerousPatterns.some(pattern => pattern.test(input));
  };

  const generateCSRFToken = (): string => {
    const token = Math.random().toString(36).substring(2) + Date.now().toString(36);
    csrfTokens.current.add(token);
    return token;
  };

  const validateCSRFToken = (token: string): boolean => {
    return csrfTokens.current.has(token);
  };

  const checkRateLimit = (username: string): boolean => {
    const now = Date.now();
    const attempts = loginAttempts.current[username] || { count: 0, lastAttempt: 0 };
    
    // Reset if more than 5 minutes have passed
    if (now - attempts.lastAttempt > 5 * 60 * 1000) {
      attempts.count = 0;
    }
    
    // Block if more than 5 attempts in 5 minutes
    if (attempts.count >= 5) {
      return false;
    }
    
    attempts.count++;
    attempts.lastAttempt = now;
    loginAttempts.current[username] = attempts;
    
    return true;
  };

  const login = (username: string, password: string) => {
    // Input validation
    const sanitizedUsername = sanitizeInput(username);
    const sanitizedPassword = sanitizeInput(password);
    
    if (!validateInput(sanitizedUsername) || !validateInput(sanitizedPassword)) {
      return false;
    }
    
    // Rate limiting
    if (!checkRateLimit(sanitizedUsername)) {
      return false;
    }
    
    const users = getAllUsers();
    const found = users.find((u: any) => u.username === sanitizedUsername && u.password === sanitizedPassword);
    if (found) {
      const userObj = { username: found.username, role: found.role };
      setUser(userObj);
      localStorage.setItem("user", JSON.stringify(userObj));
      // Clear login attempts on successful login
      delete loginAttempts.current[sanitizedUsername];
      return true;
    }
    return false;
  };

  const logout = () => {
    setUser(null);
    localStorage.removeItem("user");
    // Clear all CSRF tokens on logout
    csrfTokens.current.clear();
    // Clear login attempts on logout
    loginAttempts.current = {};
  };

  const register = (username: string, password: string) => {
    // Input validation
    const sanitizedUsername = sanitizeInput(username);
    const sanitizedPassword = sanitizeInput(password);
    
    if (!validateInput(sanitizedUsername) || !validateInput(sanitizedPassword)) {
      return "Nieprawidłowe dane wejściowe.";
    }
    
    const users = getAllUsers();
    if (users.find((u: any) => u.username === sanitizedUsername)) {
      return "Taki login już istnieje.";
    }
    const newUser = { username: sanitizedUsername, password: sanitizedPassword, role: "user" };
    const updated = [...users, newUser];
    saveUsers(updated);
    return true;
  };

  const changePassword = (oldPass: string, newPass: string, repeat: string) => {
    if (!user) return "Musisz być zalogowany.";
    
    // Input validation
    const sanitizedOldPass = sanitizeInput(oldPass);
    const sanitizedNewPass = sanitizeInput(newPass);
    const sanitizedRepeat = sanitizeInput(repeat);
    
    if (!validateInput(sanitizedOldPass) || !validateInput(sanitizedNewPass) || !validateInput(sanitizedRepeat)) {
      return "Nieprawidłowe dane wejściowe.";
    }
    
    const users = getAllUsers();
    const idx = users.findIndex((u: any) => u.username === user.username);
    if (idx === -1) return "Użytkownik nie istnieje.";
    if (users[idx].password !== sanitizedOldPass) return "Stare hasło jest nieprawidłowe.";
    if (sanitizedNewPass.length < 6) return "Nowe hasło musi mieć min. 6 znaków.";
    if (sanitizedNewPass !== sanitizedRepeat) return "Nowe hasła nie są zgodne.";
    users[idx].password = sanitizedNewPass;
    saveUsers(users);
    return true;
  };

  const isRateLimited = (username: string): boolean => {
    const now = Date.now();
    const attempts = loginAttempts.current[username] || { count: 0, lastAttempt: 0 };
    
    // Reset if more than 5 minutes have passed
    if (now - attempts.lastAttempt > 5 * 60 * 1000) {
      return false;
    }
    
    // Return true if more than 5 attempts in 5 minutes
    return attempts.count >= 5;
  };

  return (
    <AuthContext.Provider value={{ user, login, logout, register, changePassword, generateCSRFToken, validateCSRFToken, isRateLimited }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error("useAuth must be used within AuthProvider");
  return ctx;
};
