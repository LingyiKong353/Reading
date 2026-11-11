# AI Agents in Action

ai! ai! ai!

Hands-on notes for learning how to build AI agents, following *AI Agents in Action, Second Edition* (Manning). There is one notebook per chapter: a summary in my own words, then the exercises step by step, with the real output and what I learned. Built with the OpenAI Agents SDK.

## Notebooks

| Notebook | Book chapter | Topics | Status |
|---|---|---|---|
| [01_agent_core_components](01_agent_core_components.ipynb) | 2 | Instructions, model settings, typed outputs, tracing, tools | In progress |

## Run it yourself

Requires Python 3.11 or later and an OpenAI API key (the API is billed separately from a ChatGPT subscription).

```bash
python -m venv venv
venv\Scripts\activate           # macOS/Linux: source venv/bin/activate
pip install -r ai-agents-in-action/requirements.txt
```

Create a file named `.env` (in this folder or the repository root) containing `OPENAI_API_KEY=your-key`, and never commit it. Then open a notebook in VS Code or Jupyter, pick the `venv` kernel, and run the cells in order.

## Credit

The exercises are adapted from the sample code for *AI Agents in Action, Second Edition* (Manning): [AI-Agent-Workflows](https://github.com/cxbxmxcx/AI-Agent-Workflows), under the Apache License 2.0 (copy in `LICENSE-AI-Agent-Workflows.txt`). Modified: converted to notebooks, with added notes. Based on upstream commit `2978e9b`.
