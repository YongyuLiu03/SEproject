// // import logo from './logo.svg';
// // import './App.css';

// import React, {useState} from 'react';
// import Login from './login';
// import Signup from './signup';
// import TakenCourses from './takenCourses';
// import Logout from './logout';

// import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';


// const App = () => {

//   const username = 
//   return (
    
//      <Router>
//         <nav>
//           <ul>
//             <li>
//               <Link to="/">Home</Link>
//             </li>
//             <li>
//               <Link to="/login">Login</Link>
//             </li>
//             <li>
//               <Link to="/signup">Signup</Link>
//             </li>
//             <li>
//               <Link to="/taken-courses">Taken Courses</Link>
//             </li>
//           </ul>
//         </nav>


//       <Routes>
//         <Route path="/" element={<Login />} />
//         <Route path="/login" element={<Login />} />
//         <Route path="/signup" element={<Signup />} />
//         <Route path="/taken-courses" element={<TakenCourses />} />
//         <Route path="/logout" element={<Logout />} />

//       </Routes>
      
//       <Logout />
//       </Router>
  

//   );
// }



// export default App;




import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './Navbar';
import Login from './Login';
import Signup from './Signup';
import Courses from './Courses';
import Recommendations from './Recommendations';

function App() {
  const [user, setUser] = useState(null);
  const [auth, setAuth] = useState(false);

  return (
    
    <Router>
      <div>
        {auth && <Navbar user={user} setAuth={setAuth} />}
        <Routes>
          <Route path="/login" element={<Login setUser={setUser} setAuth={setAuth} />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/courses" element={auth ? <Courses user={user} /> : <Login setUser={setUser} setAuth={setAuth} />} />
          <Route path="/recommendations" element={auth ? <Recommendations user={user} /> : <Login setUser={setUser} setAuth={setAuth} />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;

