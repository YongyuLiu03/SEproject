import React from 'react';
import { useNavigate } from 'react-router-dom';

const Logout = () => {
  const navigate = useNavigate();
  
  const isLoggedIn = () => {
    return localStorage.getItem('token') !== null;
  };

  
  const handleLogout = () => {
    localStorage.removeItem('token');
    navigate('/login'); 
    // You might also want to make a logout API call to invalidate the token server-side
  };
  
  return (
    isLoggedIn() ? (
      <div>
        {/* You can style this as you prefer */}
        <button onClick={handleLogout}>Log Out</button>
      </div>
    ) : null
  );
};

export default Logout;
