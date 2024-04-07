// import logo from './logo.svg';
// import './App.css';

import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Login from './login';
import Signup from './signup';
import TakenCourses from './takenCourses';
import Logout from './logout';

function App() {
  return (
    <>
     <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
        <Route path="/taken-courses" element={<TakenCourses />} />
        <Route path="/logout" element={<Logout />} />

        {/* Add additional routes as needed */}
      </Routes>
       <Logout />
       </Router>
    </>

  );
}



export default App;



