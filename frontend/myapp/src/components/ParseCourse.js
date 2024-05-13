import React, { useState, useEffect } from 'react';
import axiosInstance from '../axiosInstance';
import { Link } from 'react-router-dom';
import { useAuth } from './AuthContext';

const ParseCourse = () => {
    const [courseDict, setCourseDict] = useState('');
    const [updateCourse, setUpdateCourse] = useState(true);
    const [parseCourse, setParseCourse] = useState(true);
    const [responses, setResponses] = useState([]);
    const {setStudent} = useAuth();

    function isObject(value) {
        return value !== null && typeof value === 'object' && Object.keys(value).length > 0;
    }

    useEffect(() => {
        const coursesExist = localStorage.getItem('coursesExist') === 'true';
        if (!coursesExist) {
            console.log("No courses exist. Starting from scratch.");
        } else {
            axiosInstance.get('/taken-courses')
            .then(response => {
                if (isObject(response.data.student.course_dict)) {
                    setResponses([response.data.student.course_dict, ...responses]);
                    localStorage.setItem('coursesExist', 'true');
                    setStudent(JSON.stringify(response.data.student));
                } else {
                    console.error('Received course_dict is not an object:', response.data.student.course_dict);
                }
            })
            .catch(error => {
                alert('Failed to update course dictionary.');
                console.error('Update error:', error);
            });
        }
    }, []);

    const handleSubmit = (e) => {
        e.preventDefault();

        axiosInstance.post('/taken-courses', {
            course_dict: parseCourse ? JSON.stringify(courseDict) : courseDict,  
            updateCourse: updateCourse,
            parseCourse: parseCourse,
        })
        .then(response => {
            if (isObject(response.data.student.course_dict)) {
                setResponses([response.data.student.course_dict, ...responses]);
                localStorage.setItem('coursesExist', 'true');
                setStudent(JSON.stringify(response.data.student));
                localStorage.setItem('student', JSON.stringify(response.data.student)); // Store student info in local storage
            } else {
                console.error('Received course_dict is not an object:', response.data.student.course_dict);
                alert('Received invalid course data.');
            }
        })
        .catch(error => {
            alert('Failed to update course dictionary.');
            console.error('Update error:', error);
            if (error.response) {
                console.error('Error status:', error.response.status);
                console.error('Error details:', error.response.data);
            }
        });
    };

    return (
        <div>
            <h1>Course History</h1>
            <form onSubmit={handleSubmit}>
                <br />
                <label>
                    Course Dictionary:
                    <textarea 
                        value={courseDict} 
                        onChange={e => setCourseDict(e.target.value)} 
                        placeholder="Enter course dictionary here"
                    />
                </label>
                <br />
                <label>
                    Update Courses (if renewing your courses):
                    <input 
                        type="checkbox" 
                        checked={updateCourse} 
                        onChange={e => setUpdateCourse(e.target.checked)} 
                    />
                </label>
                <br />

                <label>
                    Parse Courses (if you are submitting plain HTML):
                    <input 
                        type="checkbox" 
                        checked={parseCourse} 
                        onChange={e => setParseCourse(e.target.checked)} 
                    />
                </label>
                <br />
                <button type="submit">Submit</button>
            </form>


            <div>
                <h2>Responses (new to old):</h2>
                {responses.length > 0 ? (
                    <div>
                        {responses.map((courses, index) => (
                        <div>
                            
                        <h2>{index+1}</h2>
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
                                        <Link to={`/course/${number}`}>
                                        Detail
                                        </Link>

                                    </tr>
                                    ))}
                                </tbody>
                                </table>
                            </div>
                            ))}
                        </div>
                                
                           
                        ))}
                    </div>
                ) : (
                    <p>No responses yet.</p>
                )}
            </div>
        </div>
    );
};

export default ParseCourse;

