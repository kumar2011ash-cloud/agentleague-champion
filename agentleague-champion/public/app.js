const form = document.getElementById('agent-form');
const output = document.getElementById('output');

form.addEventListener('submit', async (event) => {
  event.preventDefault();

  const topic = document.getElementById('topic').value.trim();
  const track = document.getElementById('track').value;

  if (!topic) {
    output.textContent = 'Please enter a project idea or problem statement.';
    return;
  }

  output.textContent = 'Generating your hackathon plan...';

  try {
    const response = await fetch('/api/agent', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ topic, track })
    });

    const data = await response.json();

    if (!response.ok) {
      output.textContent = data.error || 'Unable to generate a response.';
      return;
    }

    output.textContent = data.plan;
  } catch (error) {
    output.textContent = 'Network error. Please check the server and try again.';
    console.error(error);
  }
});
