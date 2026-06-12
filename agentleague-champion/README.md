# AgentLeague Champion

AgentLeague Champion is a Microsoft Agents League hackathon assistant designed to help teams create a winning submission quickly. It generates fully structured project plans, Azure architecture guidance, demo flows, and submission checklists for reasoning-based agent solutions.

## What makes it strong

- Built for the **Agents League** hackathon with Reasoning Agents, Creative Apps, and Enterprise Agents support.
- Produces polished assets for **Innovation Studios** submission.
- Includes guidance for **Azure OpenAI**, **Microsoft Foundry**, **Agent Framework**, and Microsoft 365 integration.
- Provides a ready-to-demo web interface and backend.

## Features

- Hackathon project plan generation
- Architecture & Azure service recommendations
- Demo flow and pitch-ready output
- Submission checklist builder
- Lightweight Express + OpenAI scaffold

## Getting started

1. Install dependencies:

```bash
npm install
```

2. Copy `.env.example` to `.env` and set your OpenAI key:

```bash
copy .env.example .env
```

3. Start the app:

```bash
npm start
```

4. Visit `http://localhost:4000`.

## Environment variables

- `OPENAI_API_KEY` — required for OpenAI or Azure OpenAI.
- `PORT` — optional, default is 4000.
- `OPENAI_API_BASE` — optional if using Azure OpenAI.

Optional Azure OpenAI configuration:

```text
OPENAI_API_BASE=https://your-azure-openai-endpoint.openai.azure.com/
OPENAI_API_TYPE=azure
OPENAI_API_VERSION=2024-12-01
OPENAI_DEPLOYMENT_NAME=your-deployment-name
```

## Project structure

- `server.js` — Express backend and API endpoint
- `agent.js` — prompt engine and AI reasoning plan generator
- `public/` — UI for entering a project idea and generating plans
- `README.md` — setup and hackathon guidance
- `architecture.md` — architecture diagram and service mapping
- `project-description.md` — submission narrative and pitch
- `submission-guide.md` — hackathon-specific checklist and assets

## How to use

1. Open the UI.
2. Enter your project idea or problem statement.
3. Select the target Agents League track.
4. Generate the plan.
5. Use the generated output for your GitHub repo, demo video, and submission text.

## Submission guidance

- Use the generated plan as the basis for your Innovation Studios project description.
- Record a 2-minute demo that follows the demo flow.
- Attach architecture diagrams and screenshots.
- Include the public GitHub repo link.
- Finalize and submit before the deadline.

## Why this entry can win

AgentLeague Champion is built to help judges quickly understand the idea, architecture, user experience, and AI value. It emphasizes Microsoft technologies and a polished submission-ready deliverable.
