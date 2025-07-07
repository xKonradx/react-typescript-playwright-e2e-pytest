import React, { useState } from "react";
import LoginForm from "../components/LoginForm";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import { Link } from "react-router-dom";

const LoginView: React.FC = () => {
  const [error, setError] = useState("");
  return (
    <Box display="flex" flexDirection="column" alignItems="center" justifyContent="center" minHeight="80vh">
      <Typography variant="h3" fontWeight={700} mb={4} role="heading" aria-level={1}>Logowanie</Typography>
      {error && <Typography color="error" mb={2} data-testid="login-error" role="alert" aria-live="polite">{error}</Typography>}
      <LoginForm onError={setError} />
      <Typography mt={2}>
        Nie masz konta? <Link to="/register" aria-label="Przejdź do strony rejestracji">Zarejestruj się</Link>
      </Typography>
    </Box>
  );
};

export default LoginView;
