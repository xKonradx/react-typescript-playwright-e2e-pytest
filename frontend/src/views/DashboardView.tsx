import React from "react";
import { useAuth } from "../context/AuthContext";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import Button from "@mui/material/Button";

const DashboardView: React.FC = () => {
  const { user } = useAuth();
  return (
    <Box p={4} minHeight="80vh">
      <Typography variant="h4" fontWeight={700} mb={2} role="heading" aria-level={1}>Dashboard</Typography>
      <Typography mb={1} role="status" aria-live="polite">Witaj, {user?.username}!</Typography>
      <Typography mb={2} role="status">Twoja rola: {user?.role}</Typography>
      <Button 
        variant="contained" 
        color="primary"
        aria-label="Przycisk dashboard"
      >
        Przycisk dashboard
      </Button>
    </Box>
  );
};

export default DashboardView;
