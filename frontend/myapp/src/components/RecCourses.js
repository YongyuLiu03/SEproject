import React, { useState, useEffect } from "react";
import axiosInstance from "../axiosInstance";

const Recommend = () => {
  const [identity, setIdentity] = useState("");
  const [intense, setIntense] = useState("");
  const [recommendations, setRecommendations] = useState([]);
  const [error, setError] = useState("");
  const [response, setResponses] = useState([]);

  function isObject(value) {
    return (
      value !== null &&
      typeof value === "object" &&
      Object.keys(value).length > 0
    );
  }

  useEffect(() => {
    const coursesExist = localStorage.getItem("coursesExist") === "true";
    if (!coursesExist) {
      console.log("No courses exist. Starting from scratch.");
    } else {
      axiosInstance
        .get("/taken-courses")
        .then((response) => {
          if (isObject(response.data.student.course_dict)) {
            setResponses(response.data.student.course_dict);
          } else {
            console.error(
              "Received course_dict is not an object:",
              response.data.student.course_dict
            );
          }
        })
        .catch((error) => {
          alert("Failed to update course dictionary.");
          console.error("Update error:", error);
        });
    }
  }, []);

  const fetchRecommendations = () => {
    axiosInstance
      .get("/rec-courses", { params: { identity, intense } })
      .then((response) => {
        if (response.data.valid) {
          console.log(response.data.recommend_courses);
          setRecommendations(response.data.recommend_courses);
          setError("");
          console.log(typeof recommendations);
        } else {
          setRecommendations(null);
          setError("No valid recommendations found.");
        }
      })
      .catch((error) => {
        setError("Failed to fetch recommendations. Please check your inputs.");
        console.error("Recommendation fetch error:", error);
      });
    console.log(recommendations);
  };

  return (
    <div>
      {response.length > 0 ? (
        <div>
          {Object.entries(response).map(([semester, courseList]) => (
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
      ) : (
        <p>No responses yet.</p>
      )}

      <h1>Recommend Courses</h1>
      <div>
        <label>
          Identity:
          <select
            value={identity}
            onChange={(e) => setIdentity(e.target.value)}
          >
            <option value="chinese">Chinese</option>
            <option value="inter">International</option>
          </select>
        </label>
        <label>
          Intense:
          <select value={intense} onChange={(e) => setIntense(e.target.value)}>
            <option value="true">True</option>
            <option value="false">False</option>
          </select>
        </label>
        <button onClick={fetchRecommendations}>Get Recommendations</button>
      </div>
      {error && <p style={{ color: "red" }}>{error}</p>}
      {recommendations &&
        Object.entries(recommendations).map(([semester, courses]) => (
          <div key={semester}>
            <h2>{semester.replace("_", " ").toUpperCase()}</h2>
            <ul>
              {courses.map((course, index) => (
                <li key={index}>{course}</li>
              ))}
            </ul>
          </div>
        ))}
    </div>
  );
};

export default Recommend;
