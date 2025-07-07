import React from "react";
import { Navigate, Outlet } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";

const ProtectedRoute: React.FC = () => {
  const { user } = useAuth();
  // Jeśli user jest null, sprawdź localStorage
  if (!user) {
    const local = localStorage.getItem("user");
    if (!local) {
      return <Navigate to="/login" replace />;
    }
  }
  // Fallback: jeśli coś pójdzie nie tak, pokaż komunikat po polsku
  if (!user || !user.username) {
    return (
      <Box display="flex" flexDirection="column" alignItems="center" justifyContent="center" minHeight="80vh">
        <Typography variant="h4" color="error" mb={2}>
          Brak dostępu
        </Typography>
        <Typography variant="body1">
          Musisz być zalogowany, aby zobaczyć tę stronę.
        </Typography>
      </Box>
    );
  }
  return <Outlet />;
};

export default ProtectedRoute;
