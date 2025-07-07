import React, { Suspense, useMemo, useState } from "react";
import { AuthProvider } from "./context/AuthContext";
import AppRouter from "./routes/AppRouter";
import { ThemeProvider, createTheme, CssBaseline } from "@mui/material";

const App: React.FC = () => {
  const [darkMode, setDarkMode] = useState(false);
  const theme = useMemo(
    () =>
      createTheme({
        palette: {
          mode: darkMode ? "dark" : "light",
        },
      }),
    [darkMode]
  );
  const toggleDarkMode = () => setDarkMode((d) => !d);

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <AuthProvider>
        <Suspense fallback={<div>Ładowanie...</div>}>
          <AppRouter darkMode={darkMode} toggleDarkMode={toggleDarkMode} />
        </Suspense>
      </AuthProvider>
    </ThemeProvider>
  );
};

export default App;
