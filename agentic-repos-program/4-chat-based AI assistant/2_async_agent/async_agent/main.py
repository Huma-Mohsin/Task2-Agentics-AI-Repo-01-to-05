import os
import asyncio
from dotenv import load_dotenv
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig, Runner

# Load environment variables
load_dotenv()

# Read the Gemini API key
my_api_key = os.getenv("GEMINI_API_KEY")
if not my_api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set.")

# Set up the external client for the Gemini API
external_client = AsyncOpenAI(
    api_key=my_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Set up the model wrapper to use Gemini with OpenAI interface
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

# Configuration for running the agent
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# Async main function to handle continuous conversation
async def main():
    # Create the agent
    myAgent = Agent(
        name="AI Assistant",
      instructions =(
        "You are a helpful AI assistant. "
        "Answer the user queries clearly and kindly, but keep your responses concise and focused. "
        "Avoid long explanations unless specifically requested. "
        "If the user asks for templates or examples, provide a short example or summarize it briefly. "
        "Always ask if the user wants more details."
    ),
        model=model
    )

    print("Welcome to AI-Chatbot! Type 'exit' or 'quit' to end the chat.\n")

    # Continuous chat loop
    while True:
        user_input = input("Ask me anything: ")
        if user_input.lower() in ["exit", "quit"]:
            print("AI-Chatbot: Goodbye! See you next time!")
            break

        # Run the agent with the user's message
        result = await Runner.run(myAgent, user_input, run_config=config)

        # Print the response from the agent
        print("AI-Chatbot:", result.final_output)

# Run the async function only if this is the main script
if __name__ == "__main__":
    asyncio.run(main())
