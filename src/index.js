import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';       // ← importa los estilos
import App from './App';    // ← importa el componente principal

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);