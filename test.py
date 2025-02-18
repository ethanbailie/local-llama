from smolagents import CodeAgent, DuckDuckGoSearchTool, LiteLLMModel

model = LiteLLMModel(
    model_id='ollama_chat/qwen2.5:14b'
)
agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=model)

agent.run("How many seconds would it take for a leopard at full speed to run through Pont des Arts?")