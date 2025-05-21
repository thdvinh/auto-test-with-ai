from mcp.server.fastmcp import FastMCP
import os

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def make_magic(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def write_file(file_path: str, content: str) -> None:
    os.makedirs("mcp-output", exist_ok=True)
    """Write content to a file"""
    with open(os.path.join("mcp-output", file_path), "w") as f:
        f.write(content)
        f.flush()


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

if __name__ == "__main__":
    # Start the server
    mcp.run()