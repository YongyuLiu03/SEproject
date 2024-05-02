import React, { useState, useEffect } from 'react';
import axiosInstance from './axiosInstance';

function Recommendations({ user }) {
  const [recommendations, setRecommendations] = useState([]);

  useEffect(() => {
    const params = { identity: 'chinese', intense: true }; // Modify as needed
    axiosInstance.get('api/rec-courses', { params })
      .then(response => {
        if (response.data.valid) {
          setRecommendations(response.data.recommend_courses);
        } else {
          alert('Cannot fulfill major requirements in four years');
        }
      })
      .catch(error => alert(`Error: ${error.response.data.message}`));
  }, [user]);

  return (
    <div>
      <h2>Recommended Courses</h2>
      {/* Display recommendations */}
    </div>
  );
}


export default Recommendations;