import React, { useState, useEffect } from 'react';
import axiosInstance from './axiosInstance';


const TempInfo = () => {
//   const [htmlInput, setHtmlInput] = useState('');
  const [untakenMajor, setUntakenMajor] = useState([]);
  const [untakenCore, setUntakenCore] = useState([]);
  const [takenElect, setTakenElect] = useState([]);
  // const [update, setUpdate] = useState(false);

  useEffect(() => {
    const getTempInfo = async () => {
        try {
          const response = await axiosInstance.get('temp-info/');
          setUntakenCore(response.data.untaken_core_courses);
          setTakenElect(response.data.taken_elective_courses);
          setUntakenMajor(response.data.untaken_major_courses);
          // setUpdate(true);
          console.log(response.data);
        } catch (error) {
          console.error("Failed to retrieve course data:", error);
        }
    };
    
    getTempInfo();
  }, []);
  


  return (
    <div className="TempInfo">
      <div>
        <h2>Untaken Major Courses</h2>
        {untakenMajor.map((courseGroup, index) => (
            <div key={index}>
            <h3>Group {index + 1}</h3>
            <ul>
              {courseGroup.map((course, courseIndex) => (
                <li key={courseIndex}>{course}</li>
              ))}
            </ul>
          </div>
        ))}

        <h2>Untaken Core Courses</h2>
        <ul>
            {untakenCore.map((course, index) => (
            <li key={index}>{course}</li>
            ))}
        </ul>

        <h2>Taken Electives</h2>
        <ul>
            {takenElect.map((course, index) => (
            <li key={index}>{course}</li>
            ))}
        </ul>
      </div>
    </div>
  );
}

export default TempInfo;