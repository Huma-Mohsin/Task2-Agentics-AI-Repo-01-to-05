# Import necessary libraries
import os  # For interacting with the operating system (used to get environment variables)
from dotenv import load_dotenv  # To load environment variables from a .env file

# Import classes from the agentic AI framework
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig, Runner

# --------------------------------------------
# Step 1: Load environment variables from .env file
# --------------------------------------------
load_dotenv()  # Loads the variables defined in your .env file into the system environment
my_api_key = os.getenv("GEMINI_API_KEY")  # Retrieves the Gemini API key

# Raise an error if the API key is not found
if not my_api_key:
    raise ValueError("GEMINI_API_KEY is not set.")  # Prevents the app from running without authentication

# --------------------------------------------
# Step 2: Initialize the external OpenAI-compatible Gemini client
# --------------------------------------------
external_client = AsyncOpenAI(
    api_key=my_api_key,  # The Gemini API key
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",  # Gemini's OpenAI-compatible API base URL
)

# --------------------------------------------
# Step 3: Define the AI model to use with Gemini
# --------------------------------------------
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",  # The Gemini model to use (a fast variant)
    openai_client=external_client  # Connect the model to the external Gemini client
)

# --------------------------------------------
# Step 4: Configure how the agent should run
# --------------------------------------------
config = RunConfig(
    model=model,  # The model defined above
    model_provider=external_client,  # The provider (Gemini client)
    tracing_disabled=True  # Disables tracing/logging for simplicity (can be enabled for debugging or observability)
)

# --------------------------------------------
# Step 5: Create the AI Agent with specific instructions
# --------------------------------------------
myAgent = Agent(
    name="QueryBot",  # Name of the chatbot
    instructions=(
        "You are a knowledgeable and friendly assistant. "
        "Answer clearly, be concise, and help users by explaining concepts in simple terms."
    ),  # Behavior and personality of the chatbot
    model=model  # Attach the model to the agent
)

# --------------------------------------------
# Step 6: Run an interactive loop to chat with the agent
# --------------------------------------------
print("Welcome to QueryBot! Type 'exit' to quit.")  # Greeting message

while True:
    # Prompt user for input
    user_input = input("\nYou: ")

    # Allow the user to exit the chatbot
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye! See you next time!")
        break  # Exit the loop and end the program

    # Call the agent synchronously using the Runner class with the user's input
    response = Runner.run_sync(myAgent, user_input, run_config=config)

    # Print the response from the agent
    print(f"QueryBot: {response.final_output}")
