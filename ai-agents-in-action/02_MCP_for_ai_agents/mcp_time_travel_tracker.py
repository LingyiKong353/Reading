import sys

from mcp.server.mcpserver import MCPServer

mcp = MCPServer("Time Travel Tracker")

# In-memory journal state (list of entries).
# It lives as long as this server process lives.
_journal = []


def log(message: str) -> None:
    """Log to stderr. Over stdio, stdout is reserved for JSON-RPC messages."""
    print(message, file=sys.stderr, flush=True)


@mcp.tool()
def record_event(entry: str) -> dict:
    """Add a new travel event to the journal."""
    _journal.append(entry)
    log(f"Event recorded: {entry}")
    return {"status": "recorded", "entry": entry}


@mcp.tool()
def load_journal() -> dict:
    """Load the current travel journal entries."""
    log("Loading journal entries...")
    return {"status": "loaded", "journal": "\n".join(_journal)}


if __name__ == "__main__":
    mcp.run(transport="sse")
