# AI Agents in Action

My hands-on notes for learning how to build AI agents, following *AI Agents in Action, Second Edition* (Manning).

There is one notebook per chapter. Each starts with a summary of the chapter in my own words, then works through the exercises step by step, with the real output, what I changed, and what I learned. The code uses the OpenAI Agents SDK.

## Notebooks

| Notebook | Book chapter | Topics | Status |
|---|---|---|---|
| [01_agent_core_components](01_agent_core_components.ipynb) | 2 | Instructions, model settings, typed outputs, tracing, tools | In progress |

More notebooks are added as I finish each chapter.

## Run it yourself

Requires Python 3.11 or later.

```bash
python -m venv venv
venv\Scripts\activate           # macOS/Linux: source venv/bin/activate
pip install -r ai-agents-in-action/requirements.txt
```

Copy `.env.example` to `.env` (in this folder or the repository root) and add your `OPENAI_API_KEY`. The OpenAI API is billed separately from a ChatGPT subscription and needs a small credit balance. Then open a notebook in VS Code or Jupyter, pick the `venv` kernel, and run the cells in order.

Never commit your `.env` file.

## Credit

The exercises are adapted from the book's sample code, [AI-Agent-Workflows](https://github.com/cxbxmxcx/AI-Agent-Workflows), under the Apache License 2.0. See [ATTRIBUTION.md](ATTRIBUTION.md).
