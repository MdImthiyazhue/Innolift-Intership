# Day 28 — Hooks & useState

## Task 01 — Name Preview
Controlled input using `useState` + `onChange`. Shows `Hello, {name}! 👋` while typing, falls back to `Hello, Guest! 👤` when empty.

## Task 02 — Theme Toggle
Boolean `useState` flips a `dark` class on `<body>` via `useEffect`, switching the whole page between light and dark mode on click.

## Files
- `NamePreview.jsx` — Task 01 component
- `ThemeToggle.jsx` — Task 02 component
- `App.jsx` / `App.css` — combines both, drop into any Vite/CRA React project's `src/` folder
- `index.html` — **standalone demo**, no build step needed. Just open it in a browser to test both tasks or record the submission video.

## Quick test
Double-click `index.html` (or open it in a browser) — both components run immediately via CDN React.

To use inside a real project instead:
```bash
npm create vite@latest my-app -- --template react
# copy NamePreview.jsx, ThemeToggle.jsx, App.jsx, App.css into src/
npm install
npm run dev
```
