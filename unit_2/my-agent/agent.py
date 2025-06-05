import os

from huggingface_hub import Agent

agent = Agent(
    model="Qwen/Qwen2.5-72B-Instruct",
    provider="nebius",
    servers=[
        {
            "command": "npx",
            "args": [
                "mcp-remote",
                "https://sperva-mcp-sentiment.hf.space/gradio_api/mcp/sse"  # Your Gradio MCP server
            ]
        }
    ],
)

agent.run()