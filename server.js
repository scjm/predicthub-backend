const express = require('express');
const { execFile } = require('child_process');
const cors = require('cors');

const app = express();
app.use(cors()); // ✅ Enable CORS for all routes

const PORT = 5001;

app.get('/api/stock', (req, res) => {
  const symbol = req.query.symbol || 'AAPL';
  console.log("⏳ Received request for symbol:", symbol);

  // ✅ Use Python from virtual environment created in Docker
  const pythonPath = '/app/venv/bin/python';

  execFile(pythonPath, ['fetch_prices.py', symbol], (error, stdout, stderr) => {
    if (error) {
      console.error('❌ Error:', error);
      return res.status(500).json({ error: 'Failed to fetch stock data Scooter' });
    }

    try {
      const data = JSON.parse(stdout);
      res.json(data);
    } catch (e) {
      console.error('❌ Parsing error:', e);
      res.status(500).json({ error: 'Invalid JSON from Python script' });
    }
  });
});

app.listen(PORT, () => {
  console.log(`✅ Server running on http://localhost:${PORT}`);
});
