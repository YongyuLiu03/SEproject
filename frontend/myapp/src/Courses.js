import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Courses({ user }) {
  const [courses, setCourses] = useState([]);

  useEffect(() => {
    if (user.coursesExist) {
      axios.get('api/taken-courses')
        .then(response => setCourses(response.data))
        .catch(error => alert(`Error: ${error.response.data.message}`));
    }
  }, [user]);

const handleInputChange = (e) => {
    setCourseInput(prev => ({ ...prev, [e.target.name]: e.target.value }));
};

const submitCourse = (e) => {
    e.preventDefault();
    axios.post('api/taken-courses', { newCourse: courseInput })
        .then(response => {
            setCourses(response.data);
            setCourseInput({ semester: '', courseId: '', courseName: '', courseCredit: '' }); // Reset form
        })
        .catch(error => alert(`Error: ${error.response.data.message}`));
};

  const handleCourseSubmit = (newCourses) => {
    axios.post('api/taken-courses', { newCourses })
      .then(response => setCourses(response.data))
      .catch(error => alert(`Error: ${error.response.data.message}`));
  };
  const [htmlInput, setHtmlInput] = useState('');
  const [courses, setCourses] = useState({});
  const [update, setUpdate] = useState(false);

  useEffect(() => {
    const getCourseDict = async () => {
      if (localStorage.getItem('coursesExist') === 'true') {
        try {
          const response = await axiosInstance.get('courses/');
          setCourses(response.data);
          // setUpdate(true);
          console.log(response.data);
        } catch (error) {
          console.error("Failed to retrieve course data:", error);
        }
      }
    };
    
    getCourseDict();
  }, []);
  
    
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axiosInstance.post('taken-courses', { courses: htmlInput});
      setCourses(response.data);
    } catch (error) {
      console.error("Error fetching data: ", error);
    }
  };




  return (
    <div>
        <h2>Taken Courses</h2>
        <form onSubmit={handleSubmit}>
        <textarea value={htmlInput} onChange={(e) => setHtmlInput(e.target.value)} />
        <button type="submit">Submit</button>
        </form>
        <ul>
            {Object.entries(courses).map(([semester, coursesList]) => (
                <li key={semester}>
                    <strong>{semester}</strong>
                    <ul>
                        {coursesList.map(course => (
                            <li key={course[0]}>{course[1]} ({course[2]} credits)</li>
                        ))}
                    </ul>
                </li>
            ))}
        </ul>
    </div>
);
}

export default Courses;