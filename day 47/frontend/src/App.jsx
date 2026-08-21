import { useEffect, useState } from "react";
import "./App.css";

// Reusable API base URL with safe local development fallback
const API_BASE_URL = (import.meta.env.VITE_API_URL || "http://localhost:5000").replace(/\/$/, "");
const API_URL = `${API_BASE_URL}/api`;

function App() {
  // =========================================================================
  // SECTION 1: Student Management State & Handlers
  // =========================================================================
  const [students, setStudents] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const [form, setForm] = useState({ name: "", email: "", course: "" });
  const [formError, setFormError] = useState("");
  const [successMsg, setSuccessMsg] = useState("");
  const [submitting, setSubmitting] = useState(false);

  // GET /api/students -> MySQL SELECT (via Flask)
  const fetchStudents = async () => {
    setLoading(true);
    setError("");
    try {
      const response = await fetch(`${API_URL}/students`);
      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.message || `Server responded with status ${response.status}`);
      }

      setStudents(data);
    } catch (err) {
      console.error("Fetch error:", err);
      if (err.message && err.message.includes("Failed to fetch")) {
        setError("Unable to connect to the backend. Please make sure the Flask server is running.");
      } else {
        setError(err.message || "Unable to load students.");
      }
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchStudents();
  }, []);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  // POST /api/students -> Validate -> MySQL INSERT (via Flask)
  const handleSubmit = async (e) => {
    e.preventDefault();
    setFormError("");
    setSuccessMsg("");

    if (!form.name.trim() || !form.email.trim() || !form.course.trim()) {
      setFormError("All fields are required.");
      return;
    }

    setSubmitting(true);
    try {
      const response = await fetch(`${API_URL}/students`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(form),
      });

      const result = await response.json();

      if (!response.ok || !result.success) {
        throw new Error(result.message || "Failed to add student.");
      }

      setStudents((prev) => [...prev, result.student]);
      setSuccessMsg(result.message || "Student added successfully!");
      setForm({ name: "", email: "", course: "" });
    } catch (err) {
      console.error("Submit error:", err);
      if (err.message && err.message.includes("Failed to fetch")) {
        setFormError("Unable to connect to the backend. Please make sure the Flask server is running.");
      } else {
        setFormError(err.message || "Unable to save student. Please try again.");
      }
    } finally {
      setSubmitting(false);
    }
  };

  // =========================================================================
  // SECTION 2: Customer Churn ML Prediction State & Handlers
  // =========================================================================
  const [predForm, setPredForm] = useState({
    tenure_months: "",
    monthly_charges: "",
    total_purchases: "",
    support_tickets: "",
  });
  const [predLoading, setPredLoading] = useState(false);
  const [predError, setPredError] = useState("");
  const [predResult, setPredResult] = useState(null);

  const handlePredChange = (e) => {
    setPredForm({ ...predForm, [e.target.name]: e.target.value });
  };

  // POST /api/predict -> Validate -> ML Model Inference (via Flask)
  const handlePredSubmit = async (e) => {
    e.preventDefault();
    setPredError("");

    const { tenure_months, monthly_charges, total_purchases, support_tickets } = predForm;

    // 1. Frontend validation: Check required non-empty
    if (
      tenure_months === "" ||
      monthly_charges === "" ||
      total_purchases === "" ||
      support_tickets === ""
    ) {
      setPredError("All 4 prediction fields are required.");
      return;
    }

    // 2. Numeric conversion & validation
    const numTenure = Number(tenure_months);
    const numCharges = Number(monthly_charges);
    const numPurchases = Number(total_purchases);
    const numTickets = Number(support_tickets);

    if (
      isNaN(numTenure) ||
      isNaN(numCharges) ||
      isNaN(numPurchases) ||
      isNaN(numTickets)
    ) {
      setPredError("All fields must be valid numeric values.");
      return;
    }

    // 3. Reject negative numbers
    if (numTenure < 0 || numCharges < 0 || numPurchases < 0 || numTickets < 0) {
      setPredError("Input values cannot be negative.");
      return;
    }

    setPredLoading(true);

    try {
      const response = await fetch(`${API_URL}/predict`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          tenure_months: numTenure,
          monthly_charges: numCharges,
          total_purchases: numPurchases,
          support_tickets: numTickets,
        }),
      });

      let data;
      try {
        data = await response.json();
      } catch (jsonErr) {
        throw new Error("Unexpected server response. Expected JSON.");
      }

      if (!response.ok || !data.success) {
        throw new Error(data.error || data.message || `Prediction failed with status ${response.status}`);
      }

      // Store prediction result in state
      setPredResult({
        prediction: data.prediction,
        churn_probability: data.churn_probability,
      });
    } catch (err) {
      console.error("Prediction error:", err);
      // Clear previous stale result on error
      setPredResult(null);

      if (err.message && (err.message.includes("Failed to fetch") || err.name === "TypeError")) {
        setPredError("Unable to connect to the backend. Please make sure the Flask server is running.");
      } else {
        setPredError(err.message || "Prediction failed due to an unexpected error.");
      }
    } finally {
      setPredLoading(false);
    }
  };

  return (
    <div className="container">
      <header className="app-header">
        <h1>Innolift Ventures Internship Platform</h1>
        <p className="app-subtitle">Student Management & Churn ML Intelligence</p>
      </header>

      {/* =================================================================== */}
      {/* SECTION 1: Student Management UI                                    */}
      {/* =================================================================== */}
      <section className="card-section">
        <h2>Student Management</h2>

        {/* Add Student Form */}
        <form className="student-form" onSubmit={handleSubmit}>
          <h3>Add Student</h3>
          <input
            type="text"
            name="name"
            placeholder="Full Name"
            value={form.name}
            onChange={handleChange}
          />
          <input
            type="email"
            name="email"
            placeholder="Email Address"
            value={form.email}
            onChange={handleChange}
          />
          <input
            type="text"
            name="course"
            placeholder="Course"
            value={form.course}
            onChange={handleChange}
          />
          <button type="submit" disabled={submitting}>
            {submitting ? "Submitting..." : "Add Student"}
          </button>

          {formError && <p className="error-text">{formError}</p>}
          {successMsg && <p className="success-text">{successMsg}</p>}
        </form>

        {/* Student List */}
        <h3>Student List</h3>

        {loading && <p className="info-text">Loading students...</p>}

        {!loading && error && <p className="error-text">{error}</p>}

        {!loading && !error && students.length === 0 && (
          <p className="empty-text">No students found.</p>
        )}

        {!loading && !error && students.length > 0 && (
          <table className="student-table">
            <thead>
              <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Email</th>
                <th>Course</th>
              </tr>
            </thead>
            <tbody>
              {students.map((s) => (
                <tr key={s.id}>
                  <td>{s.id}</td>
                  <td>{s.name}</td>
                  <td>{s.email}</td>
                  <td>{s.course}</td>
                </tr>
              ))}
            </tbody>
          </table>
        )}

        <button className="retry-btn" onClick={fetchStudents}>
          Refresh List
        </button>
      </section>

      {/* =================================================================== */}
      {/* SECTION 2: Customer Churn ML Prediction UI (Day 47)                */}
      {/* =================================================================== */}
      <section className="card-section prediction-section">
        <h2>Customer Churn Prediction (ShopIQ ML Model)</h2>
        <p className="section-description">
          Enter customer usage and support metrics to predict the likelihood of customer churn.
        </p>

        <form className="prediction-form" onSubmit={handlePredSubmit}>
          <div className="form-grid">
            <div className="form-group">
              <label htmlFor="tenure_months">Tenure (months):</label>
              <input
                id="tenure_months"
                type="number"
                name="tenure_months"
                placeholder="e.g. 12"
                min="0"
                step="1"
                value={predForm.tenure_months}
                onChange={handlePredChange}
              />
            </div>

            <div className="form-group">
              <label htmlFor="monthly_charges">Monthly Charges ($):</label>
              <input
                id="monthly_charges"
                type="number"
                name="monthly_charges"
                placeholder="e.g. 75.50"
                min="0"
                step="0.01"
                value={predForm.monthly_charges}
                onChange={handlePredChange}
              />
            </div>

            <div className="form-group">
              <label htmlFor="total_purchases">Total Purchases:</label>
              <input
                id="total_purchases"
                type="number"
                name="total_purchases"
                placeholder="e.g. 5"
                min="0"
                step="1"
                value={predForm.total_purchases}
                onChange={handlePredChange}
              />
            </div>

            <div className="form-group">
              <label htmlFor="support_tickets">Support Tickets:</label>
              <input
                id="support_tickets"
                type="number"
                name="support_tickets"
                placeholder="e.g. 2"
                min="0"
                step="1"
                value={predForm.support_tickets}
                onChange={handlePredChange}
              />
            </div>
          </div>

          <button
            type="submit"
            className="predict-btn"
            disabled={predLoading}
          >
            {predLoading ? "Generating Prediction..." : "Predict Churn Risk"}
          </button>

          {predError && <p className="error-text pred-error">{predError}</p>}
        </form>

        {/* Prediction Results Display */}
        {predResult && (
          <div
            className={`prediction-result-card ${
              predResult.prediction === "Churn" ? "result-churn" : "result-no-churn"
            }`}
          >
            <h3>Prediction Result</h3>
            <div className="result-details">
              <div className="result-row">
                <span className="result-label">Churn Risk:</span>
                <span
                  className={`badge ${
                    predResult.prediction === "Churn"
                      ? "badge-churn"
                      : "badge-no-churn"
                  }`}
                >
                  {predResult.prediction}
                </span>
              </div>
              <div className="result-row">
                <span className="result-label">Churn Probability:</span>
                <span className="result-value">
                  {Math.round(predResult.churn_probability * 100)}%
                  <span className="raw-prob"> ({predResult.churn_probability.toFixed(3)})</span>
                </span>
              </div>
              <p className="result-summary">
                {predResult.prediction === "Churn"
                  ? "High risk of customer attrition. Proactive retention measures are recommended."
                  : "Low risk of customer attrition. Customer engagement appears healthy."}
              </p>
            </div>
          </div>
        )}
      </section>
    </div>
  );
}

export default App;

