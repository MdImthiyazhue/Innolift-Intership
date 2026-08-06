-- ============================================================
-- Day 35 - Basics of SQL
-- Seed data for portfolio_db (matches index.html content)
-- ============================================================

USE portfolio_db;

-- ------------------------------------------------------------
-- Profile
-- ------------------------------------------------------------
INSERT INTO profile (full_name, title, bio, career_objective, email, phone, linkedin_url, github_url)
VALUES (
    'Mohamed Imthiyaz',
    'B.Tech AI & Data Science Student',
    'AI & Data Science undergraduate maintaining a 9.4 CGPA, currently completing a Full Stack AI Developer Internship at Innolift Ventures. Enjoys turning data and ideas into working products.',
    'To grow as an AI/ML engineer and full-stack developer by building real-world, data-driven applications.',
    'your.email@example.com',
    '+91 00000 00000',
    'https://linkedin.com/in/mohamed-imthiyas-44i16/',
    'https://github.com/MdImthiyazhue'
);

-- ------------------------------------------------------------
-- Education
-- ------------------------------------------------------------
INSERT INTO education (qualification, institution, year_range, score)
VALUES (
    'B.Tech - Artificial Intelligence & Data Science',
    'B.S. Abdur Rahman Crescent Institute of Science and Technology',
    '2023 - 2027 (5th Semester)',
    '9.4 CGPA'
);

-- ------------------------------------------------------------
-- Skills
-- ------------------------------------------------------------
INSERT INTO skills (category, skill_name) VALUES
('Programming', 'Python'),
('Programming', 'JavaScript'),
('Programming', 'SQL'),
('Web Development', 'HTML5'),
('Web Development', 'CSS3'),
('Web Development', 'Flask'),
('Web Development', 'Node.js'),
('Web Development', 'Express'),
('AI & Data Science', 'Machine Learning'),
('AI & Data Science', 'TensorFlow / Keras'),
('AI & Data Science', 'Pandas & NumPy'),
('Tools & Database', 'MySQL'),
('Tools & Database', 'SQLite'),
('Tools & Database', 'Git & GitHub'),
('Tools & Database', 'Jupyter / Google Colab');

-- ------------------------------------------------------------
-- Projects
-- ------------------------------------------------------------
INSERT INTO projects (title, description, tech_stack) VALUES
('ShopIQ - Telco Customer Churn Prediction',
 'A binary classification project predicting telecom customer churn using the Telco dataset, covering EDA, feature engineering, and model comparison.',
 'Python, React, Flask, MySQL, Docker'),

('Vehicle Image Classification (CNN)',
 'A 4-class image classifier (Car, Bike, Bus, Truck) built with TensorFlow/Keras, using data augmentation and a Conv2D architecture on Google Colab.',
 'TensorFlow, Keras, CNN'),

('Certificate Authenticity Validator',
 'A Smart India Hackathon project using machine learning to verify the authenticity of academic certificates and flag forged documents.',
 'Machine Learning, Python'),

('AwareScore - LLM Awareness Framework',
 'A research framework evaluating situational and affective awareness in large language models, presented at BSACIST AI Summit.',
 'Research, LLMs');

-- ------------------------------------------------------------
-- Certifications
-- ------------------------------------------------------------
INSERT INTO certifications (title, description) VALUES
('Full Stack AI Developer Internship', 'Innolift Ventures - Crescent Batch'),
('Research Paper Accepted', 'ICETCI 2026 - Evaluating Situational and Affective Awareness in LLMs'),
('AI Summit Presenter', 'BSACIST - Selected Research Abstract'),
('Smart India Hackathon', 'ML-based Certificate Authenticity Validator');

-- ------------------------------------------------------------
-- Sample contact message (for testing the messages table)
-- ------------------------------------------------------------
INSERT INTO messages (sender_name, sender_email, message)
VALUES ('Test Recruiter', 'recruiter@example.com', 'Hi Imthiyaz, impressive portfolio! Would love to connect.');
