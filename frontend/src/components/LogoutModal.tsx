import React from "react";
import Dialog from "@mui/material/Dialog";
import DialogActions from "@mui/material/DialogActions";
import DialogContent from "@mui/material/DialogContent";
import DialogTitle from "@mui/material/DialogTitle";
import Button from "@mui/material/Button";

interface LogoutModalProps {
  onConfirm: () => void;
  onCancel: () => void;
}

const LogoutModal: React.FC<LogoutModalProps> = ({ onConfirm, onCancel }) => (
  <Dialog 
    open 
    onClose={onCancel}
    aria-labelledby="logout-dialog-title"
    aria-describedby="logout-dialog-description"
  >
    <DialogTitle id="logout-dialog-title">Czy na pewno chcesz się wylogować?</DialogTitle>
    <DialogContent id="logout-dialog-description">
      Po wylogowaniu utracisz dostęp do chronionych funkcji aplikacji.
    </DialogContent>
    <DialogActions>
      <Button 
        onClick={onConfirm} 
        color="error" 
        variant="contained"
        aria-label="Potwierdź wylogowanie"
      >
        Potwierdź
      </Button>
      <Button 
        onClick={onCancel} 
        variant="outlined"
        aria-label="Anuluj wylogowanie"
      >
        Anuluj
      </Button>
    </DialogActions>
  </Dialog>
);

export default LogoutModal;
