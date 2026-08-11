import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// Proxy /api calls to the Flask backend during development so the
// React app can call fetch('/api/students') without CORS issues
// and without hardcoding http://localhost:5000 everywhere.
export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    proxy: {
      "/api": {
        target: "http://127.0.0.1:5000",
        changeOrigin: true,
      },
    },
  },
});
