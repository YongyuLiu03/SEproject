import React, { createContext, useContext, useState, useEffect } from "react";

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [authState, setAuthState] = useState({
    token: localStorage.getItem("token") || null,
    username: localStorage.getItem("username") || null,
    student: JSON.parse(localStorage.getItem("student")) || null, // Parse the student data if it exists
  });

  const login = (token, username, coursesExist) => {
    localStorage.setItem("token", token);
    localStorage.setItem("username", username);
    localStorage.setItem("coursesExist", coursesExist);
    setAuthState({ token, username });
  };

  const logout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("username");
    localStorage.removeItem("student");
    setAuthState({ token: null, username: null, student: null });
  };

  const setStudent = (student) => {
    localStorage.setItem("student", JSON.stringify(student)); // Ensure student data is serialized
    setAuthState((prevState) => ({ ...prevState, student }));
  };

  // Initialize state from local storage
  useEffect(() => {
    const token = localStorage.getItem("token");
    const username = localStorage.getItem("username");
    const student = JSON.parse(localStorage.getItem("student")); // Parse the student JSON string

    if (token && username) {
      setAuthState({ token, username, student });
    }
  }, []);

  return (
    <AuthContext.Provider value={{ ...authState, login, logout, setStudent }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
