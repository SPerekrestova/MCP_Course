from smolagents.mcp_client import MCPClient

with MCPClient(
    {"url": "https://sperva-mcp-sentiment.hf.space/gradio_api/mcp/sse",
     "transport": "sse"}
) as tools:
    # Tools from the remote server are available
    print("\n".join(f"{t.name}: {t.description}" for t in tools))
