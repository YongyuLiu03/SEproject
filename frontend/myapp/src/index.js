import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import { AuthProvider } from './components/AuthContext';

import { createRoot } from 'react-dom/client'; 

const container = document.getElementById('root');
const root = createRoot(container); // Create a root instance

root.render(
  <React.StrictMode>
    <AuthProvider>
      <App />
    </AuthProvider>
  </React.StrictMode>
);
