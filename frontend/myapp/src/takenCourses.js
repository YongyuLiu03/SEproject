import React, { useState, useEffect, Component } from 'react';
import axiosInstance from './axiosInstance';

const TakenCourses = () => {
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

    <div className="TakenCourses">
      <form onSubmit={handleSubmit}>
        <textarea value={htmlInput} onChange={(e) => setHtmlInput(e.target.value)} />
        {/* <input type='checkbox' value='hide_grade' checked={hideGrade} onChange={() => sethideGrade(!hideGrade)} />hide grade */}
        <button type="submit">Submit</button>
      </form>
      <div>
        {Object.entries(courses).map(([semester, courseList]) => (
          <div key={semester}>
            <h3>{semester}</h3>
            <table>
              <thead>
                <tr>
                  <th>Course number</th>
                  <th>Course name</th>
                  <th>Credit</th>
                </tr>
              </thead>
              <tbody>
                {courseList.map(([number, name, credit], index) => (
                  <tr key={index}>
                    <td>{number}</td>
                    <td>{name}</td>
                    <td>{credit}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        ))}
      </div>
    </div>

  );
}

export default TakenCourses;