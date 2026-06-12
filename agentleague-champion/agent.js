const { OpenAI } = require('openai');

const SYSTEM_PROMPT = `You are AgentLeague Champion, an expert Microsoft hackathon assistant. You help teams win the Agents League by generating complete submission assets for a reasoning-focused AI agent. Your output should be structured, persuasive, and clearly aligned with Microsoft Foundry, Azure OpenAI, and the Agents League judging criteria.`;

function createOpenAIClient() {
  const apiKey = process.env.OPENAI_API_KEY;
  if (!apiKey) {
    throw new Error('OPENAI_API_KEY is required to generate AI responses. Update .env before running the agent.');
  }

  const clientConfig = { apiKey };
  if (process.env.OPENAI_API_BASE) {
    clientConfig.baseURL = process.env.OPENAI_API_BASE;
  }

  return new OpenAI(clientConfig);
}

async function runAgentPlan({ topic, track }) {
  const client = createOpenAIClient();
  const userPrompt = `A hackathon team needs a winning Agents League submission. The user has provided this challenge: "${topic}". The target track is "${track}".

Produce a polished markdown response with the following sections:

## Project Concept
- One-sentence mission statement
- What problem it solves and why it's compelling for Agents League

## Core Features
- 4 to 6 feature bullets with direct user benefit

## Architecture & Azure Services
- Azure OpenAI / Azure Cognitive Services
- Microsoft Foundry / Agent Framework integration path
- Optional Azure services like Azure Functions, Cosmos DB, Azure App Service, and Microsoft 365 connectors

## Demo Flow
- Step-by-step user demo in 5 actions

## Submission Checklist
- What to include for Innovation Studios submission: code repo, video, architecture diagram, demo, pitch

## Why it wins
- A short statement on why this idea stands out in Agents League

Use clear headings and keep the plan concise.`;

  const response = await client.chat.completions.create({
    model: 'gpt-4.1-mini',
    messages: [
      { role: 'system', content: SYSTEM_PROMPT },
      { role: 'user', content: userPrompt }
    ],
    max_tokens: 900,
    temperature: 0.75
  });

  return response.choices[0]?.message?.content?.trim() || 'Unable to generate a plan at this time.';
}

module.exports = { runAgentPlan };
