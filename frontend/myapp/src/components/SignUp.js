import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axiosInstance from '../axiosInstance';

const SignUp = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate();

    const handleSignUp = async (e) => {
        e.preventDefault();
        try {
            const response = await axiosInstance.post('/signup', {
                username,
                password
            });
            if (response.status === 201) {
                navigate('/login');
                alert('User created successfully');
            } else {
                alert('Signup failed');
            }
        } catch (error) {
            if (error.response) {
                // The request was made and the server responded with a status code
                // that falls out of the range of 2xx
                alert(JSON.stringify(error.response.data));
            } else {
                // The request was made but no response was received or an error occurred
                // in setting up the request that triggered an Error
                alert('Error during signup: ' + error.message);
            }
        }
    };


    return (
        <div>
            <h1>Sign Up</h1>
            <form onSubmit={handleSignUp}>
                <input type="text" placeholder="Username" value={username} onChange={e => setUsername(e.target.value)} />
                <input type="password" placeholder="Password" value={password} onChange={e => setPassword(e.target.value)} />
                <button type="submit">Sign Up</button>
            </form>
        </div>
    );
};

export default SignUp;
