import React, { useState } from 'react';
import axiosInstance from './axiosInstance';


const TakenCourses = () => {
  const [htmlInput, setHtmlInput] = useState('');
  const [courses, setCourses] = useState({});
  const [hideGrade, sethideGrade] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axiosInstance.post('courses/', { html: htmlInput, hideGrade: hideGrade });
      setCourses(response.data);
    } catch (error) {
      console.error("Error fetching data: ", error);
    }
  };

  return (
    <div className="App">
      <form onSubmit={handleSubmit}>
        <textarea value={htmlInput} onChange={(e) => setHtmlInput(e.target.value)} />
        <input type='checkbox' value='hide_grade' checked={hideGrade} onChange={() => sethideGrade(!hideGrade)} />hide grade
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
                  {!hideGrade && <th>Grade</th>}
                </tr>
              </thead>
              <tbody>
                {courseList.map(([number, name, credit, grade], index) => (
                  <tr key={index}>
                    <td>{number}</td>
                    <td>{name}</td>
                    <td>{credit}</td>
                    {!hideGrade && <td>{grade}</td>}
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