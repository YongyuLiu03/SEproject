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
  };
  
  return (
    isLoggedIn() ? (
      <div>
        <button onClick={handleLogout}>Log Out</button>
      </div>
    ) : (<div>
      You are not logged in. Why are you here?
    </div>)
  );
};

export default Logout;
