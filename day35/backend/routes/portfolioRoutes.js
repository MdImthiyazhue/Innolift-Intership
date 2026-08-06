// ============================================================
// Day 35 - Portfolio API routes (CRUD backed by MySQL)
// ============================================================
const express = require('express');
const router = express.Router();
const { pool } = require('../config/db');

// ---------- PROFILE ----------
router.get('/profile', async (req, res) => {
    try {
        const [rows] = await pool.query('SELECT * FROM profile LIMIT 1');
        res.json(rows[0] || {});
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

// ---------- EDUCATION ----------
router.get('/education', async (req, res) => {
    try {
        const [rows] = await pool.query('SELECT * FROM education');
        res.json(rows);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

// ---------- SKILLS ----------
router.get('/skills', async (req, res) => {
    try {
        const [rows] = await pool.query('SELECT * FROM skills ORDER BY category');
        res.json(rows);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

// ---------- PROJECTS ----------
router.get('/projects', async (req, res) => {
    try {
        const [rows] = await pool.query('SELECT * FROM projects');
        res.json(rows);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

router.post('/projects', async (req, res) => {
    try {
        const { title, description, tech_stack } = req.body;
        if (!title) return res.status(400).json({ error: 'title is required' });

        const [result] = await pool.query(
            'INSERT INTO projects (title, description, tech_stack) VALUES (?, ?, ?)',
            [title, description || null, tech_stack || null]
        );
        res.status(201).json({ id: result.insertId, title, description, tech_stack });
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

// ---------- CERTIFICATIONS ----------
router.get('/certifications', async (req, res) => {
    try {
        const [rows] = await pool.query('SELECT * FROM certifications');
        res.json(rows);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

// ---------- CONTACT MESSAGES ----------
// Called by the portfolio's contact form
router.post('/messages', async (req, res) => {
    try {
        const { sender_name, sender_email, message } = req.body;
        if (!sender_name || !sender_email || !message) {
            return res.status(400).json({ error: 'sender_name, sender_email, and message are required' });
        }

        const [result] = await pool.query(
            'INSERT INTO messages (sender_name, sender_email, message) VALUES (?, ?, ?)',
            [sender_name, sender_email, message]
        );
        res.status(201).json({ id: result.insertId, message: 'Message received. Thank you!' });
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

// Admin-style listing of received messages
router.get('/messages', async (req, res) => {
    try {
        const [rows] = await pool.query('SELECT * FROM messages ORDER BY submitted_at DESC');
        res.json(rows);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

module.exports = router;
