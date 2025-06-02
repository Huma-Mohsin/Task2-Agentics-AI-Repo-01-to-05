# Chainlit is a Python library designed to help you build and deploy conversational AI applications quickly and easily.

# Here’s what Chainlit does:

# Creates interactive chat apps where users can type messages and get responses from AI models (like OpenAI’s GPT or others).

# Handles the communication flow between the user interface (the chat window) and the backend AI logic.

# Provides tools and decorators (like @cl.on_message) to define how your app reacts to user input asynchronously.

# Lets you run your app locally or deploy it so others can interact with your AI agent.

# Supports integration with various AI models (OpenAI, Gemini, etc.) through simple code.

# In short:
# Chainlit makes it super easy to turn your AI code into a user-friendly chat app without building all the frontend from scratch. It’s perfect for prototyping or showcasing AI agents.


import os                             # To interact with the operating system environment variables
from dotenv import load_dotenv       # To load environment variables from a .env file
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, Runner, RunConfig  # Import agent framework components
import chainlit as cl                # Import Chainlit library to build the chat app
from agents.run import RunConfig, Runner, Agent  # (redundant import of same classes, but included anyway)
import asyncio                      # To handle asynchronous programming


# Load environment variables from the .env file into the system environment
load_dotenv()

# Retrieve the Gemini API key from the environment variables
my_api_key = os.getenv("GEMINI_API_KEY")

# If the API key is missing, raise an error to notify the user
if not my_api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")

# Setup the Gemini AI client using AsyncOpenAI with the provided API key and base URL
external_client = AsyncOpenAI(
    api_key=my_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Define the AI chat completions model to be used with Gemini's API
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",   # Specify the Gemini model version
    openai_client=external_client  # Use the Gemini API client created above
)

# Create the configuration for running the AI agent
config = RunConfig(
    model=model,                  # Model to use
    model_provider=external_client,  # Provider handling API calls
    tracing_disabled=True         # Disable tracing for performance or privacy reasons
)

# Define an async function decorated with Chainlit to handle incoming messages
@cl.on_message
async def main(message: cl.Message):
    # Create an agent instance with a name, instructions, and the AI model
    agent = Agent(
        name="GeminiAgent",                   # Name of the agent
        instructions="You are a helpful assistant.Be  concise as well as specific to the query",  # Role/behavior instructions
        model=model                           # AI model assigned to the agent
    )
    # Run the agent asynchronously with the user's message and configuration
    result = await Runner.run(agent, message.content, run_config=config)
    # Send the AI's response back to the user via Chainlit's messaging interface
    await cl.Message(content=result.final_output).send()

# To run this Chainlit app, use the terminal command:
# chainlit run app.py
