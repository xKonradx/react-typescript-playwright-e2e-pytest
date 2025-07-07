import React from "react";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";

const NotFound: React.FC = () => (
  <Box display="flex" flexDirection="column" alignItems="center" justifyContent="center" minHeight="80vh">
    <Typography variant="h2" fontWeight={700} mb={2}>404</Typography>
    <Typography>Nie znaleziono strony.</Typography>
  </Box>
);

export default NotFound;
