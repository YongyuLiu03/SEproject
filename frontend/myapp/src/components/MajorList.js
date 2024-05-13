import React from "react";
import { Link } from "react-router-dom";

const MajorList = () => {
  const core_map = {
    "Algorithmic Thinking": "AT",
    "Experimental Discovery in the Natural World": "ED",
    "Humanistic Perspectives on China/China Arts-HPC/CA": "HPC",
    "Interdisciplinary Perspectives on China": "IPC",
    Language: "Language",
    Math: "Math",
    "Science, Technology and Society": "STS",
    "Social Science Perspective on China": "SSPC",
  };

  return (
    <div>
      <h1>Majors</h1>
      <ul>
        <li key="cs">
          <Link to={`/majors/cs`}>CS</Link>
        </li>
      </ul>
      <h1>Cores</h1>
      <ul>
        {Object.entries(core_map).map(([major, abbreviation]) => (
          <li key={abbreviation}>
            <Link to={`/majors/${abbreviation}`}>{major}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default MajorList;
