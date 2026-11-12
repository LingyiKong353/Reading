"""The time-travel tracker agent, packaged as an MCP server.

Instead of exposing record_event and load_journal directly, this server
exposes one tool, time_tracker, and a whole agent runs behind it. Any other
agent can now hand journaling work to this one over MCP.
"""

import sys

from agents import Agent, Runner, flush_traces, function_tool, trace
from dotenv import load_dotenv
from mcp.server.mcpserver import MCPServer

load_dotenv("C:/Users/kongl/Starting-something-new/.env")

mcp = MCPServer("Time Travel Tracker Agent")

# The journal lives as long as this server process lives.
_journal = []


def log(message: str) -> None:
    """Log to stderr so the log never mixes with the protocol."""
    print(message, file=sys.stderr, flush=True)


@function_tool
def record_event(entry: str) -> dict:
    """Add a new travel event to the journal."""
    _journal.append(entry)
    log(f"Event recorded: {entry}")
    return {"status": "recorded", "entry": entry}


@function_tool
def load_journal() -> dict:
    """Load the current travel journal entries."""
    log("Loading journal entries...")
    return {"status": "loaded", "journal": "\n".join(_journal)}


tracker_agent = Agent(
    name="Time Tracker Agent",
    instructions="""You are a time tracking journaling agent.
Always use the 'load_journal' tool at the start to get past entries.
For a new event, call 'record_event' to save it.
If asked for a summary or to show the journal, output all recorded events.""",
    tools=[record_event, load_journal],
)


@mcp.tool()
async def time_tracker(request: str) -> str:
    """Hand a request to the time-travel journal agent.

    Use it to record a new trip, or to ask for the full travel history.
    """
    with trace("time_tracker (MCP-hosted agent)"):
        result = await Runner.run(tracker_agent, request)
    flush_traces()  # send the trace now, before the server can be stopped
    return result.final_output


if __name__ == "__main__":
    mcp.run(transport="sse")
