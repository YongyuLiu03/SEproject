import React from 'react';
import axiosInstance from './axiosInstance';

function Navbar({ user, setAuth }) {
  const logout = () => {
    axiosInstance.get('api/logout')
      .then(() => {
        setAuth(false);
      })
      .catch(error => alert(`Error: ${error.response.data.message}`));
  };

  return (
    <div>
      <h1>Welcome, {user.username}</h1>
      <button onClick={logout}>Logout</button>
    </div>
  );
}

export default Navbar;
