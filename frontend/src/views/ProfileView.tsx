import React, { useState } from "react";
import { useAuth } from "../context/AuthContext";
import Box from "@mui/material/Box";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import Typography from "@mui/material/Typography";

const ProfileView: React.FC = () => {
  const { user, changePassword } = useAuth();
  const [oldPass, setOldPass] = useState("");
  const [newPass, setNewPass] = useState("");
  const [repeat, setRepeat] = useState("");
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  if (!user) return null;

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setError("");
    setSuccess("");
    const result = changePassword(oldPass, newPass, repeat);
    if (result !== true) {
      setError(result as string);
      return;
    }
    setSuccess("Hasło zostało zmienione!");
    setOldPass(""); setNewPass(""); setRepeat("");
  };

  return (
    <Box display="flex" flexDirection="column" alignItems="center" justifyContent="center" minHeight="80vh">
      <Typography variant="h3" fontWeight={700} mb={4} role="heading" aria-level={1}>Mój profil</Typography>
      <Typography mb={2}>Zalogowany jako: <b>{user.username}</b></Typography>
      {error && <Typography color="error" mb={2} data-testid="profile-error" role="alert" aria-live="polite">{error}</Typography>}
      {success && <Typography color="primary" mb={2} data-testid="profile-success" role="alert" aria-live="polite">{success}</Typography>}
      <Box component="form" onSubmit={handleSubmit} sx={{ width: 300, display: 'flex', flexDirection: 'column', gap: 2 }} role="form" aria-label="Formularz zmiany hasła">
        <TextField 
          label="Stare hasło" 
          type="password" 
          value={oldPass} 
          onChange={e => setOldPass(e.target.value)} 
          required 
          fullWidth 
          inputProps={{
            'aria-label': 'Stare hasło użytkownika',
            'aria-required': 'true'
          }}
        />
        <TextField 
          label="Nowe hasło" 
          type="password" 
          value={newPass} 
          onChange={e => setNewPass(e.target.value)} 
          required 
          fullWidth 
          inputProps={{
            'aria-label': 'Nowe hasło użytkownika',
            'aria-required': 'true'
          }}
        />
        <TextField 
          label="Powtórz nowe hasło" 
          type="password" 
          value={repeat} 
          onChange={e => setRepeat(e.target.value)} 
          required 
          fullWidth 
          inputProps={{
            'aria-label': 'Powtórz nowe hasło użytkownika',
            'aria-required': 'true'
          }}
        />
        <Button 
          type="submit" 
          variant="contained" 
          color="primary" 
          fullWidth
          aria-label="Zmień hasło użytkownika"
        >
          Zmień hasło
        </Button>
      </Box>
    </Box>
  );
};

export default ProfileView; 