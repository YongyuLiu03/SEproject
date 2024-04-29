import React, { useState, useEffect } from 'react';
import axiosInstance from './axiosInstance';


const ViewCoreCourses = () => {
  const [htmlInput, setHtmlInput] = useState('');
  const [courses, setCourses] = useState({});
  // const [update, setUpdate] = useState(false);

  useEffect(() => {
    const getCoreDict = async () => {
        try {
          const response = await axiosInstance.get('core-courses/');
          setCourses(response.data);
          // setUpdate(true);
          console.log(response.data);
        } catch (error) {
          console.error("Failed to retrieve course data:", error);
        }
    };
    
    getCoreDict();
  }, []);
  
    
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

export default ViewCoreCourses;