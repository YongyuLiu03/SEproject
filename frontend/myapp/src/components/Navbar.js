import React from "react";
import { Link, useNavigate } from "react-router-dom";
import { useAuth } from "./AuthContext";
import axiosInstance from "../axiosInstance";

const Navbar = () => {
  const navigate = useNavigate();
  const { username, logout } = useAuth();

  const handleLogout = async () => {
    try {
      await axiosInstance.get("/logout");
      logout();
      localStorage.removeItem("token");
      navigate("/login");
    } catch (error) {
      console.error("Logout failed", error);
    }
  };

  return (
    <nav>
      <ul>
        <li>
          <Link to="/main">Home</Link>
        </li>

        {username ? (
          <>
            <li>Welcome, {username}!</li>
            <li>
              <Link to="/history">Course History</Link>
            </li>
            <li>
              <Link to="/recommend">Recommend</Link>
            </li>
            <li>
              <button onClick={handleLogout}>Logout</button>
            </li>
          </>
        ) : (
          <>
            <h1> Yor are not logged in</h1>
            <li>
              <Link to="/login">Login</Link>
            </li>
            <li>
              <Link to="/signup">Signup</Link>
            </li>
          </>
        )}
        <li>
          <Link to="/majors"> Major/Cores</Link>
        </li>
      </ul>
    </nav>
  );
};

export default Navbar;
