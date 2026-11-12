from mcp.server.mcpserver import MCPServer

mcp = MCPServer("Research Tools")


@mcp.tool()
def get_research_sources() -> list[str]:
    """Provides a list of research sources."""
    return ["Wikipedia", "Google", "YouTube"]
