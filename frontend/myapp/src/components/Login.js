import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "./AuthContext";
import axiosInstance from "../axiosInstance";

const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();
  const { login } = useAuth();

  const handleLogin = (e) => {
    e.preventDefault();
    axiosInstance
      .post("/login", { username, password })
      .then((response) => {
        console.log(response);
        login(response.data.token, username, response.data.coursesExist);
        alert("Logged in successfully");
        navigate("/");
      })
      .catch((error) => {
        const errorMessage = error.response
          ? error.response.data.error
          : error.message;
        alert(`Error: ${errorMessage}`);
      });
  };

  return (
    <div>
      <h1>Login</h1>
      <form onSubmit={handleLogin}>
        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button type="submit">Log In</button>
      </form>
    </div>
  );
};

export default Login;
