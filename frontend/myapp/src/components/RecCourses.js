import React, { useState } from 'react';
import axiosInstance from '../axiosInstance';

const Recommend = () => {
    const [identity, setIdentity] = useState('');
    const [intense, setIntense] = useState('');
    const [recommendations, setRecommendations] = useState([]);
    const [error, setError] = useState('');

    const fetchRecommendations = () => {
        axiosInstance.get('/rec-courses', { params: { identity, intense } })
            .then(response => {
                if (response.data.valid) {
                    console.log(response.data.recommend_courses);
                    setRecommendations(response.data.recommend_courses);
                    setError('');
                    console.log(typeof(recommendations))
                } else {
                    setRecommendations(null);
                    setError('No valid recommendations found.');
                }
            })
            .catch(error => {
                setError('Failed to fetch recommendations. Please check your inputs.');
                console.error('Recommendation fetch error:', error);
            });
        console.log(recommendations);
    };

    return (
        <div>
            <h1>Recommend Courses</h1>
            <div>
                <label>
                    Identity:
                    <select value={identity} onChange={e => setIdentity(e.target.value)}>
                        <option value="chinese">Chinese</option>
                        <option value="inter">International</option>
                    </select>
                </label>
                <label>
                    Intense:
                    <select value={intense} onChange={e => setIntense(e.target.value)}>
                        <option value="true">True</option>
                        <option value="false">False</option>
                    </select>
                </label>
                <button onClick={fetchRecommendations}>Get Recommendations</button>
            </div>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            {recommendations && Object.entries(recommendations).map(([semester, courses]) => (
                <div key={semester}>
                    <h2>{semester.replace('_', ' ').toUpperCase()}</h2>
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
