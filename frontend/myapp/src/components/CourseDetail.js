import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axiosInstance from "../axiosInstance";

const CourseDetail = () => {
  const { courseNumber } = useParams();
  const [course, setCourse] = useState(null);

  useEffect(() => {
    axiosInstance
      .get(`/courses/${courseNumber}`)
      .then((response) => {
        setCourse(response.data);
        console.log(response.data);
      })
      .catch((error) => console.error("Error fetching course details:", error));
  }, [courseNumber]);

  if (!course) {
    return <div>Course {courseNumber} is not stored in our database :(</div>;
  }

  return (
    <div>
      <h2>
        {courseNumber} {course.course.name}
      </h2>
      <p>
        <strong>Credits:</strong> {course.course.credit}
      </p>
      <p>
        <strong>Description:</strong> {course.course.description}{" "}
      </p>
      <h2>Prerequisites</h2>
      {course.prerequisites.length > 0 ? (
        <ul>
          {course.prerequisites.map((prereq, index) => (
            <li key={index}>{prereq.name}</li>
          ))}
        </ul>
      ) : (
        <p>No prerequisites listed.</p>
      )}
      <h2>Fulfills Major Requirements For</h2>
      {course.majors.length > 0 ? (
        <ul>
          {course.majors.map((major, index) => (
            <li key={index}>{major.name}</li>
          ))}
        </ul>
      ) : (
        <p>No major requirements fulfilled by this course.</p>
      )}
    </div>
  );
};

export default CourseDetail;
