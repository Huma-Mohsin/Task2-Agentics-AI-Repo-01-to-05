from agents import Agent, AsyncOpenAI, RunConfig, Runner, OpenAIChatCompletionsModel
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
my_api_key = os.getenv("GEMINI_API_KEY")

# Check for API key
if not my_api_key:
    raise ValueError("GEMINI_API_KEY is not set in the .env file")

# Configure external Gemini model (OpenAI-style interface)
external_client = AsyncOpenAI(
    api_key=my_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# Create the agent
my_agent = Agent(
    name="Pediatrician",
    instructions=(
    "You are a professional pediatrician with expertise in child health and development. "
    "Provide clear, concise, and practical answers to questions about children's health. "
    "Limit responses to essential information only, using clinical insight where helpful. "
    "Avoid general disclaimers or unnecessary elaboration. "
    "Offer medically sound suggestions or next steps based on symptoms, and maintain a calm, informative tone."
)

)

while True:
    user_input = input("Ask a question about children's health: ")
    if user_input.lower() == 'exit':
        print("Exiting the Pediatrician Agent. Goodbye!")
        break

    response = Runner.run_sync(my_agent, user_input, run_config=config)
    cleaned_output = (response.final_output)

    print("Pediatrician:", cleaned_output)
