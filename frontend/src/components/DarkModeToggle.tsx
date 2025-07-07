import React from "react";
import IconButton from "@mui/material/IconButton";
import Brightness4Icon from "@mui/icons-material/Brightness4";
import Brightness7Icon from "@mui/icons-material/Brightness7";

interface DarkModeToggleProps {
  darkMode: boolean;
  toggleDarkMode: () => void;
}

const DarkModeToggle: React.FC<DarkModeToggleProps> = ({ darkMode, toggleDarkMode }) => {
  return (
    <IconButton 
      color="inherit" 
      onClick={toggleDarkMode} 
      data-testid="darkmode-toggle"
      aria-label={darkMode ? "Przełącz na tryb jasny" : "Przełącz na tryb ciemny"}
      aria-pressed={darkMode}
    >
      {darkMode ? <Brightness7Icon aria-hidden="true" /> : <Brightness4Icon aria-hidden="true" />}
    </IconButton>
  );
};

export default DarkModeToggle;
