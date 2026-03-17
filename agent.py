from phi.agent import Agent
from phi.model.openai import OpenAIChat
import os

agent = Agent(
    model=OpenAIChat(
        id="gpt-4o-mini",
        api_key = os.getenv("OPENAI_API_KEY")
    ),
    description="You are a helpful coding assistant",
)