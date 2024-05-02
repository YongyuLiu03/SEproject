// import React, { useState, useEffect } from 'react';
// import { Link, useNavigate } from 'react-router-dom';
// import axiosInstance from './axiosInstance';

// const Login = () => {
//   const navigate = useNavigate();
//   const [username, setUsername] = useState('');
//   const [password, setPassword] = useState('');
//   const [loginError, setLoginError] = useState('');
//   const [isLoggedIn, setIsLoggedIn] = useState(false);

//   useEffect(() => {
//     const token = localStorage.getItem('token');
//     setIsLoggedIn(!!token); 
//   }, []);

//   const handleLogin = async (e) => {
//     e.preventDefault();
//     try {
//       const response = await axiosInstance.post('login/', { username, password });
//       console.log(response);
//       localStorage.setItem('token', response.data.token);
//       localStorage.setItem('coursesExist', response.data.courseExists);
//       localStorage.setItem('username', username);

//       navigate('/');
//     //   navigate.push('/submit-courses'); // Redirect to course submission form
//     } catch (error) {
//       console.error("Login failed:", error.response.data);
//       const errorMessage = error.response.data.error || "Login failed. Please try again.";
//       setLoginError(errorMessage);
//     }
//   };

//   const handleLogout = async () => {
//     try {
//       await axiosInstance.post('logout/');
//       localStorage.removeItem('token');
//       setIsLoggedIn(false);
//       navigate('/');
//     } catch (error) {
//       console.error("Error during logout:", error.response);
//     }
//   };

//   if (isLoggedIn) {
//     return (
//       <div>
//         <p>{username}, You are already logged in.</p>
//         <button onClick={handleLogout}>Log out</button>
//       </div>
//     );
//   }

//   return (
//     <div>
//       <form onSubmit={handleLogin}>
//         <input value={username} onChange={(e) => setUsername(e.target.value)} placeholder="Username" />
//         <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Password" />
//         <button type="submit">Log In</button>
//         {loginError && <div className="login-error">{loginError}</div>}
//       </form>
//       <p>New user? <Link to="/signup">Sign up</Link></p>
//     </div>
//   );
// };

// export default Login;

import React, { useState } from 'react';
import axios from 'axios';
import axiosInstance from './axiosInstance';

function Login({ setUser, setAuth }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = () => {
    axiosInstance.post('api/login', { username, password })
      .then(response => {
        setUser(response.data);
        setAuth(true);
      })
      .catch(error => alert(`Error: ${error.response.data.message}`));
  };

  return (
    <div>
      <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} placeholder="Username" />
      <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Password" />
      <button onClick={handleLogin}>Login</button>
    </div>
  );
}

export default Login;
