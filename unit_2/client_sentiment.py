import os

import gradio as gr
from smolagents import InferenceClientModel, CodeAgent, MCPClient

try:
    mcp_client = MCPClient(
        {"url": "https://sperva-mcp-sentiment.hf.space/gradio_api/mcp/sse",
         "transport": "sse"}
    )
    tools = mcp_client.get_tools()

    model = InferenceClientModel(token=os.getenv("HF_TOKEN"))
    agent = CodeAgent(tools=[*tools], model=model)

    demo = gr.ChatInterface(
        fn=lambda message, history: agent.run(message),
        type="messages",
        examples=["What is the sentiment of this text? I love programming!"],
        title="Agent with MCP Tools",
        description="This is a simple agent that uses MCP tools to answer questions.",
    )

    demo.launch()
finally:
    mcp_client.disconnect()