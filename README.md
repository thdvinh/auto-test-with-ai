# auto-test-with-ai
Applying AI in automation testing

# Installation

## Prerequisites
Must be pre-installed on system:
- Python
- Go
- Nodejs
- Ollama

## Step by step
Install MCP Python SDK
```
pip install mcp[cli]
```

Install mcphost
```
go install github.com/mark3labs/mcphost@latest
```

Command to start MCP host:
```
mcphost -m openai:gpt-4o-mini `
 --config .\.mcp.json `
 --system-prompt .\trial-system-prompt.json `
 --debug
```