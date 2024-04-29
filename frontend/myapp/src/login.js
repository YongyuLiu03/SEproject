import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import axiosInstance from './axiosInstance';

const LoginForm = () => {
  const navigate = useNavigate();
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [loginError, setLoginError] = useState('');
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  useEffect(() => {
    const token = localStorage.getItem('token');
    setIsLoggedIn(!!token); // Set to true if token exists, false otherwise
  }, []);


  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await axiosInstance.post('login/', { username, password });
      // Save the token in local storage or state
      console.log(response);
      localStorage.setItem('token', response.data.token);
      localStorage.setItem('coursesExist', response.data.courseExists);
      navigate('/taken-courses');
    //   navigate.push('/submit-courses'); // Redirect to course submission form
    } catch (error) {
      console.error("Login failed:", error.response.data);
      const errorMessage = error.response.data.error || "Login failed. Please try again.";
      setLoginError(errorMessage);
    }
  };


  const handleLogout = async () => {
    try {
      await axiosInstance.post('logout/');
      localStorage.removeItem('token');
      setIsLoggedIn(false);
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
      <form onSubmit={handleLogin}>
        <input value={username} onChange={(e) => setUsername(e.target.value)} placeholder="Username" />
        <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Password" />
        <button type="submit">Log In</button>
        {loginError && <div className="login-error">{loginError}</div>}
      </form>
      <p>New user? <Link to="/signup">Sign up</Link></p>
    </div>
  );
};

export default LoginForm;
