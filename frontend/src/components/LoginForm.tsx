import React, { useId, useState, useEffect } from "react";
import { useAuth } from "../context/AuthContext";
import { useNavigate } from "react-router-dom";
import Box from "@mui/material/Box";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";

interface Props {
  onError: (msg: string) => void;
}

const LoginForm: React.FC<Props> = ({ onError }) => {
  const { login, generateCSRFToken, isRateLimited } = useAuth();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState<{ username?: string; password?: string }>({});
  const [csrfToken, setCsrfToken] = useState("");
  const usernameId = useId();
  const passwordId = useId();
  const navigate = useNavigate();

  useEffect(() => {
    setCsrfToken(generateCSRFToken());
  }, [generateCSRFToken]);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    const newErrors: { username?: string; password?: string } = {};
    
    if (!username) {
      newErrors.username = "Podaj login";
    }
    if (!password) {
      newErrors.password = "Podaj hasło";
    } else if (password.length < 6) {
      newErrors.password = "Hasło musi mieć min. 6 znaków";
    }
    
    setErrors(newErrors);
    
    if (Object.keys(newErrors).length > 0) {
      return;
    }
    
    // Check rate limiting
    if (isRateLimited(username)) {
      onError("Zbyt wiele prób logowania. Spróbuj ponownie za 5 minut. (Rate limit exceeded)");
      return;
    }
    
    if (!login(username, password)) {
      onError("Nieprawidłowy login lub hasło");
      return;
    }
    onError("");
    navigate("/dashboard");
  };

  return (
    <Box component="form" onSubmit={handleSubmit} sx={{ width: 300, display: 'flex', flexDirection: 'column', gap: 2 }} role="form" aria-label="Formularz logowania">
      <input type="hidden" name="csrf_token" value={csrfToken} />
      <TextField
        id={usernameId}
        label="Login"
        value={username}
        onChange={e => setUsername(e.target.value)}
        fullWidth
        error={!!errors.username}
        helperText={errors.username}
        aria-describedby={errors.username ? `${usernameId}-error` : undefined}
        aria-invalid={!!errors.username}
        inputProps={{
          'aria-label': 'Login użytkownika',
          'aria-required': 'true'
        }}
      />
      <TextField
        id={passwordId}
        label="Hasło"
        type="password"
        value={password}
        onChange={e => setPassword(e.target.value)}
        fullWidth
        error={!!errors.password}
        helperText={errors.password}
        aria-describedby={errors.password ? `${passwordId}-error` : undefined}
        aria-invalid={!!errors.password}
        inputProps={{ 
          minLength: 6,
          'aria-label': 'Hasło użytkownika',
          'aria-required': 'true'
        }}
      />
      <Button 
        type="submit" 
        variant="contained" 
        color="primary" 
        fullWidth
        aria-label="Zaloguj się do systemu"
      >
        Zaloguj
      </Button>
    </Box>
  );
};

export default LoginForm;
