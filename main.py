from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled
from dotenv import load_dotenv
from my_tools.tools import add, get_weather
import os

set_tracing_disabled(True)
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
base_url = os.getenv("GEMINI_BASE_URL")
model_name = os.getenv("GEMINI_MODEL_NAME")


client = AsyncOpenAI(api_key=api_key, base_url=base_url)

model = OpenAIChatCompletionsModel(
    openai_client=client,
    model=model_name
)

agent = Agent(
    name="Helpful Agent",
    instructions="You are a helpful Asistant.",
    model=model,
    tools=[add, get_weather]
)

prompt = input("Enter your Question : ")
result = Runner.run_sync(agent, prompt)
print(f"Agent:{result.final_output}")