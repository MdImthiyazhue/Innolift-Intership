-- ============================================================
-- Day 35 - Basics of SQL
-- Portfolio Website Database Schema
-- Author: Mohamed Imthiyaz
-- ============================================================

-- 1. Create the database
CREATE DATABASE IF NOT EXISTS portfolio_db;
USE portfolio_db;

-- ------------------------------------------------------------
-- 2. Profile table  (header / hero / about section)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS profile (
    id            INT AUTO_INCREMENT PRIMARY KEY,
    full_name     VARCHAR(100)  NOT NULL,
    title         VARCHAR(150)  NOT NULL,
    bio           TEXT,
    career_objective TEXT,
    email         VARCHAR(100),
    phone         VARCHAR(20),
    linkedin_url  VARCHAR(255),
    github_url    VARCHAR(255),
    created_at    TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ------------------------------------------------------------
-- 3. Education table
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS education (
    id            INT AUTO_INCREMENT PRIMARY KEY,
    qualification VARCHAR(150) NOT NULL,
    institution   VARCHAR(200) NOT NULL,
    year_range    VARCHAR(50),
    score         VARCHAR(50)
);

-- ------------------------------------------------------------
-- 4. Skills table
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS skills (
    id            INT AUTO_INCREMENT PRIMARY KEY,
    category      VARCHAR(100) NOT NULL,   -- e.g. Programming, Web Development
    skill_name    VARCHAR(100) NOT NULL
);

-- ------------------------------------------------------------
-- 5. Projects table
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS projects (
    id            INT AUTO_INCREMENT PRIMARY KEY,
    title         VARCHAR(150) NOT NULL,
    description   TEXT,
    tech_stack    VARCHAR(255)            -- comma-separated tags
);

-- ------------------------------------------------------------
-- 6. Certifications table
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS certifications (
    id            INT AUTO_INCREMENT PRIMARY KEY,
    title         VARCHAR(150) NOT NULL,
    description   VARCHAR(255)
);

-- ------------------------------------------------------------
-- 7. Contact messages table (stores portfolio contact-form submissions)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS messages (
    id            INT AUTO_INCREMENT PRIMARY KEY,
    sender_name   VARCHAR(100) NOT NULL,
    sender_email  VARCHAR(100) NOT NULL,
    message       TEXT NOT NULL,
    submitted_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
