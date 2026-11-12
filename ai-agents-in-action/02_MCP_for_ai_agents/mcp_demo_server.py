from mcp.server.mcpserver import MCPServer

mcp = MCPServer("DemoServer")

def log(output: str, file_name: str = "server_output.log"):
    """Log output to a file"""
    with open(file_name, "a") as log_file:
        log_file.write(output + "\n")

@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Return a personalized greeting for the given name"""
    log(f"Received request for greeting: {name}")
    return f"Greetings, {name}! (from resource)"

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two integers and return the sum"""
    log(f"Adding {a} and {b}")
    return a + b

@mcp.prompt()
def welcome(name: str) -> str:
    """Generate a welcome message using the greeting resource"""
    greeting_text = get_greeting(name)
    log(f"Creating welcome message for: {name}")
    return f"{greeting_text} How can I assist you today?"
