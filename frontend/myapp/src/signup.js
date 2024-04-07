import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axiosInstance from './axiosInstance';

const SignupForm = () => {
  const navigate = useNavigate();
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [signupError, setSignupError] = useState('');
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  // Add additional state for other user details as necessary
  useEffect(() => {
    const token = localStorage.getItem('token');
    setIsLoggedIn(!!token); // Set to true if token exists, false otherwise
  }, []);

  const handleSignup = async (e) => {
    e.preventDefault();
    try {
      await axiosInstance.post('signup/', { username, password /* other user details */ });
      navigate('/login'); // Redirect to login page after successful signup
    } catch (error) {
      console.error("Signup failed:", error.response);
    //   const errorMessage = error.response.data || "Signup failed. Please try again.";
      const errorMessage = error.response && error.response.data ? JSON.stringify(error.response.data) : "Signup failed. Please try again.";
      setSignupError(errorMessage);
    }
  };


  const handleLogout = async () => {
    try {
      await axiosInstance.post('logout/');
      localStorage.removeItem('token');
      navigate('/login');
    } catch (error) {
      console.error("Error during logout:", error.response);
    }
  };


  if (isLoggedIn) {
    return (
      <div>
        <p>You are already logged in.</p>
        <button onClick={handleLogout}>Log out</button>
      </div>
    );
  }

  return (
    <div>
      <form onSubmit={handleSignup}>
        <input value={username} onChange={(e) => setUsername(e.target.value)} placeholder="Username" />
        <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Password" />
        {/* Include additional fields as necessary */}
        <button type="submit">Sign Up</button>
        {signupError && <div className="signup-error">{signupError}</div>}

      </form>
    </div>
  );
};

export default SignupForm;

