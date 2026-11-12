"""Mini FS: wraps the full filesystem server but exposes only one tool.

The ready-made filesystem server offers 16 tools, including write and move.
This wrapper is itself an MCP server. It calls the real server behind the
scenes and only lets agents list a directory, nothing else.
"""

import os

from agents.mcp import MCPServerStdio
from mcp.server.mcpserver import MCPServer

mcp = MCPServer("Mini FS")

# The only folder the wrapped server may see: this experiments folder.
SANDBOX = os.path.dirname(os.path.abspath(__file__))


@mcp.tool(name="list_directory", description="List all files in the sandbox.")
async def list_directory() -> str:
    """Return the sandbox folder's contents as a single string."""
    async with MCPServerStdio(
        name="filesystem",
        params={
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-filesystem@2.2.0", SANDBOX],
        },
        client_session_timeout_seconds=60,
    ) as fs:
        result = await fs.call_tool("list_directory", {"path": SANDBOX})
        return result.content[0].text
