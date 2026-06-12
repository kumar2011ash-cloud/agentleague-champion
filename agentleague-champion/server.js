const express = require('express');
const path = require('path');
const cors = require('cors');
const bodyParser = require('body-parser');
const dotenv = require('dotenv');
const { runAgentPlan } = require('./agent');

dotenv.config();
const app = express();
const port = process.env.PORT || 4000;

app.use(cors());
app.use(bodyParser.json());
app.use(express.static(path.join(__dirname, 'public')));

app.get('/health', (req, res) => {
  res.json({ status: 'ok', project: 'AgentLeague Champion' });
});

app.post('/api/agent', async (req, res) => {
  try {
    const { topic, track } = req.body;

    if (!topic || !track) {
      return res.status(400).json({ error: 'Missing topic or track in request body.' });
    }

    const plan = await runAgentPlan({ topic, track });
    res.json({ plan });
  } catch (error) {
    console.error('Agent error:', error);
    res.status(500).json({ error: 'Failed to generate agent response.' });
  }
});

app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.listen(port, () => {
  console.log(`AgentLeague Champion running on http://localhost:${port}`);
});
