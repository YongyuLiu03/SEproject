import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import CourseDetail from './components/CourseDetail';
import Login from './components/Login';
import Main from './components/Main';
import MajorDetail from './components/MajorDetail';
import MajorList from './components/MajorList';
import NotFound from './components/NotFound';
import Recommend from './components/RecCourses';
import SignUp from './components/SignUp';
import ParseCourse from './components/ParseCourse';
import Navbar from './components/Navbar';


const App = () => {
    return (
      
        <Router>
            <Navbar />
            <Routes>
                <Route path="/" element={<Main />} /> 
                <Route path="/login" element={<Login />} /> 
                <Route path="/signup" element={<SignUp />} /> 
                <Route path="/*" element={<NotFound />} /> 
                <Route path="/course/:name" element={<CourseDetail />} /> 
                <Route path="/recommend" element={<Recommend />} /> 
                <Route path="/history" element={<ParseCourse />} /> 
                <Route path="/majors" element={<MajorList />} />
                <Route path="/majors/:name" element={<MajorDetail />} />
            </Routes>
        </Router>
    );
};

export default App;
