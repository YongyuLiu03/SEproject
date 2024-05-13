import React, { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import axiosInstance from "../axiosInstance";

const MajorDetail = () => {
  const { name } = useParams();
  const [req, setReq] = useState(null);

  useEffect(() => {
    axiosInstance
      .get(`/majors/${name}`)
      .then((response) => {
        setReq(response.data.requirements);
      })
      .catch((error) => console.error("Error fetching course details:", error));
  }, [name]); 

  if (!req) {
    return <div>Major {name} is not stored in our database :(</div>;
  }

  return (
    <div>
      <h1> {name} </h1>
      {req.map((requirement, index) => (
        <div key={index}>
          <h2>
            Requirement {index + 1}: {requirement[1]} Courses
          </h2>
          <table>
            <thead>
              <tr>
                <th>Course ID</th>
                <th>Course Name</th>
                <th>Credits</th>
                <th>Description</th>
              </tr>
            </thead>
            <tbody>
              {requirement[2].map((course, courseIndex) => (
                <tr key={course.id}>
                  <td>{course.id}</td>
                  <td>{course.name}</td>
                  <td>{course.credit}</td>
                  <td>{course.description}</td>
                  <Link to={`/course/${course.id}`}>Detail</Link>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      ))}
    </div>
  );
};

export default MajorDetail;
