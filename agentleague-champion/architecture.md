# Architecture Diagram

```mermaid
flowchart LR
  A[User Browser] -->|Enter project idea| B[AgentLeague Champion UI]
  B -->|Submit request| C[Express Backend]
  C -->|Forward prompt| D[OpenAI / Azure OpenAI]
  D -->|Return structured plan| C
  C -->|Return content| B
  B -->|Render plan| A

  subgraph Azure Stack
    D
    E[Azure App Service / Static Web App]
    F[Azure Functions]
    G[Cosmos DB / Azure SQL]
  end

  C -->|Optional data storage| G
  C -->|Optional hosted API| E
  C -->|Optional workflow triggers| F

  click D "https://learn.microsoft.com/en-us/azure/cognitive-services/openai/"
```

## Architecture components

- **User Browser**: The front-end UI for idea entry, track selection, and plan generation.
- **Express Backend**: Hosts the API, validates requests, and orchestrates AI prompt execution.
- **OpenAI / Azure OpenAI**: Powers the reasoning logic, generating structured hackathon deliverables.
- **Agent Layer**: Encapsulates the prompt engineering, track alignment, and submission-aware output.
- **Azure services**: Optional extension points for deployment, storage, and workflow automation.

## Microsoft technology mapping

- **Azure OpenAI**: Core large-language model for reasoning, planning, and pitch generation.
- **Microsoft Foundry**: Can host the agent orchestration layer and support multi-step workflows.
- **Agent Framework**: The design mirrors agent planning, action selection, and response generation.
- **Azure App Service / Static Web Apps**: Deploy the UI and backend for a production-ready demo.
- **Cosmos DB / Azure SQL**: Store user prompts, generated plans, and submission history if extended.
- **Azure Functions**: Add event-driven logic for advanced feature expansion.
