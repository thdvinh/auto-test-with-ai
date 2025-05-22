# auto-test-with-ai
Applying AI in automation testing

## Table of Contents

- [Demonstrate MCP host](#demonstrate-mcp-host)
    - [Installation](#installation)
        - [Prerequisites](#prerequisites)
        - [Step by step](#step-by-step)

## Demonstrate MCP host

### Installation

#### Prerequisites
Must be pre-installed on system:
- Python
- Go
- Nodejs
- Ollama

### Step by step
Install MCP Python SDK
```
pip install mcp[cli]
```

Install mcphost
```
go install github.com/mark3labs/mcphost@latest
```

### How to use

Command to start MCP host:
- With OpenAI:
```open
mcphost -m openai:gpt-4o-mini `
 --config .\.mcp.json `
 --system-prompt .\trial-system-prompt.json `
 --debug
```

- With Ollama models (not all models could use tools):
```
mcphost -m ollama:{{model-name}} `
 --config .\.mcp.json `
 --system-prompt .\trial-system-prompt.json `
 --debug
```

### Final thought

Comparison between using OpenAI & Ollama

Category | OpenAI | Ollama
---------|--------|-------
Complexity | Low | High
Local resources requirement | Low | High
Cost | Low ~ High (depend on model) | Zero
Speed | High | Low ~ Medium
Usability | High (OpenAI models are pretty good in using tool) | Low (not all models are able to use tool, some model cannot use tool well)
