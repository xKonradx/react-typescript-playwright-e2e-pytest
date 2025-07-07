import { useEffect, useState, useCallback } from "react";

export function useDarkMode(): [boolean, (v: boolean) => void] {
  const [dark, setDark] = useState(() => {
    const stored = localStorage.getItem("darkmode");
    return stored ? stored === "true" : false;
  });

  useEffect(() => {
    document.documentElement.setAttribute("data-theme", dark ? "dark" : "light");
    localStorage.setItem("darkmode", String(dark));
  }, [dark]);

  const set = useCallback((v: boolean) => setDark(v), []);
  return [dark, set];
}
