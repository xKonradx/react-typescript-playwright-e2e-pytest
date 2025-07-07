import React, { useMemo, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import LogoutModal from "./LogoutModal";
import DarkModeToggle from "./DarkModeToggle";
import AppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import Button from "@mui/material/Button";
import Typography from "@mui/material/Typography";

interface NavbarProps {
  darkMode: boolean;
  toggleDarkMode: () => void;
}

const Navbar: React.FC<NavbarProps> = ({ darkMode, toggleDarkMode }) => {
  const { user, logout } = useAuth();
  const [showModal, setShowModal] = useState(false);
  const navigate = useNavigate();

  const links = useMemo(() => {
    if (!user) return [{ to: "/login", label: "Logowanie" }];
    const base = [
      { to: "/dashboard", label: "Dashboard" },
      { to: "/profile", label: "Mój profil" },
    ];
    if (user.role === "admin") base.push({ to: "/admin", label: "Admin Panel" });
    return base;
  }, [user]);

  const handleLogout = () => setShowModal(true);
  const confirmLogout = () => {
    logout();
    setShowModal(false);
    // Przekieruj na stronę logowania
    navigate("/login", { replace: true });
    window.location.href = "/login";
  };

  return (
    <AppBar position="static" color="default" elevation={1}>
      <Toolbar>
        <Typography variant="h6" sx={{ flexGrow: 1 }}>
          {links.map((l) => (
            <Button key={l.to} color="inherit" component={Link} to={l.to} sx={{ textTransform: 'none', mr: 2 }}>
              {l.label}
            </Button>
          ))}
        </Typography>
        <DarkModeToggle darkMode={darkMode} toggleDarkMode={toggleDarkMode} />
        {user && (
          <>
            <Typography sx={{ ml: 2 }}>{user.username}</Typography>
            <Button color="inherit" onClick={handleLogout} sx={{ ml: 2 }}>
              Wyloguj
            </Button>
            {showModal && <LogoutModal onConfirm={confirmLogout} onCancel={() => setShowModal(false)} />}
          </>
        )}
      </Toolbar>
    </AppBar>
  );
};

export default React.memo(Navbar);
