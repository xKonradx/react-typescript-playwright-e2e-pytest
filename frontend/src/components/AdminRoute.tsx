import { Navigate, Outlet } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";

const AdminRoute = () => {
  const { user } = useAuth();
  
  if (!user) {
    return <Navigate to="/login" replace />;
  }
  
  if (user.role !== "admin") {
    return (
      <Box display="flex" flexDirection="column" alignItems="center" justifyContent="center" minHeight="80vh">
        <Typography variant="h4" color="error" mb={2}>
          Access Denied
        </Typography>
        <Typography variant="body1">
          Nie masz uprawnień do dostępu do tej strony.
        </Typography>
      </Box>
    );
  }
  
  return <Outlet />;
};

export default AdminRoute;
