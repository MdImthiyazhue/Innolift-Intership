function StudentCard(props) {
  return (
    <div className="card">

      <h2>{props.name}</h2>

      <p>
        <strong>Department:</strong> {props.department}
      </p>

      <p>
        <strong>College:</strong> {props.college}
      </p>

      <p>
        <strong>Email:</strong> {props.email}
      </p>

      <h3>Skills</h3>

      <ul>
        {props.skills.map((skill, index) => (
          <li key={index}>{skill}</li>
        ))}
      </ul>

      <hr />

    </div>
  );
}

export default StudentCard;