from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
import ollama

# Create server parameters for stdio connection
server_params = StdioServerParameters(
    command="python",  # Executable
    args=["mcp_stdio_server.py"],  # Optional command line arguments
    env=None,  # Optional environment variables
)


# Optional: create a sampling callback
async def handle_sampling_message(
    message: types.CreateMessageRequestParams,
) -> types.CreateMessageResult:
    return types.CreateMessageResult(
        role="assistant",
        content=types.TextContent(
            type="text",
            text="Hello, world! from model",
        ),
        model="gpt-3.5-turbo",
        stopReason="endTurn",
    )


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write, sampling_callback=handle_sampling_message
        ) as session:
            # Initialize the connection
            await session.initialize()

            # List available resources
            resources = await session.list_resources()
            print("Resources:", resources)

            # List available tools
            tools = await session.list_tools()
            print("Tools:", tools)

            # Read a resource
            content, mime_type = await session.read_resource("greeting://Alice")
            print("Greeting:", content, mime_type)

            # Call a tool
            result = await session.call_tool("add", arguments={"a": "1", "b": "2"})
            print("Tool result:", result)

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())