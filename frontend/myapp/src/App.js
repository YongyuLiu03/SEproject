// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;

import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [htmlInput, setHtmlInput] = useState('');
  const [courses, setCourses] = useState({});

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:8000/api/courses/', { html: htmlInput });
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
                  <th>Course Name</th>
                  <th>Grade</th>
                </tr>
              </thead>
              <tbody>
                {courseList.map(([name, grade], index) => (
                  <tr key={index}>
                    <td>{name}</td>
                    <td>{grade}</td>
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

export default App;



