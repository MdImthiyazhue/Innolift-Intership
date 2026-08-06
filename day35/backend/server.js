// ============================================================
// Day 35 - Express server connected to MySQL (portfolio_db)
// ============================================================
const express = require('express');
const cors = require('cors');
require('dotenv').config();

const { testConnection } = require('./config/db');
const portfolioRoutes = require('./routes/portfolioRoutes');

const app = express();
const PORT = process.env.PORT || 5000;

app.use(cors());
app.use(express.json());

// Health check
app.get('/', (req, res) => {
    res.json({ status: 'ok', message: 'Portfolio API is running' });
});

app.use('/api', portfolioRoutes);

// 404 handler
app.use((req, res) => {
    res.status(404).json({ error: 'Route not found' });
});

app.listen(PORT, async () => {
    console.log(`🚀 Server running at http://localhost:${PORT}`);
    await testConnection();
});
