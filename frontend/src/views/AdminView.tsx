import React from "react";
import { useAuth } from "../context/AuthContext";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import Button from "@mui/material/Button";

const AdminView: React.FC = () => {
  const { user } = useAuth();
  return (
    <Box p={4} minHeight="80vh">
      <Typography variant="h4" fontWeight={700} mb={2} role="heading" aria-level={1}>Admin Panel</Typography>
      <Typography mb={2} role="status" aria-live="polite">Witaj, {user?.username}! Jesteś adminem.</Typography>
      <Button 
        variant="contained" 
        color="primary"
        aria-label="Przycisk administratora"
      >
        Przycisk admina
      </Button>
    </Box>
  );
};

export default AdminView;
