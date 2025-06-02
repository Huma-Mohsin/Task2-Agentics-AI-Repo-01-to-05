from litellm import completion #litellm: Ek wrapper library hai jo multiple LLMs (Large Language Models) ke sath kaam karne ko simplify karti hai.
import os # os: Operating System ke sath interact karne ke liye use hota hai, jaise ki environment variables ko access karna.
from dotenv import load_dotenv 

load_dotenv()# load_dotenv: Ye function .env file se environment variables ko load karta hai, jisse sensitive information jaise API keys ko securely handle kiya ja sake.

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")

# def openai():
#     response = completion(
#         model="openai/gpt-4o",
#         messages=[{ "content": "Hello, how are you?","role": "user"}]
#     )

#     print(response)

def gemini():
    response = completion(
        model="gemini/gemini-1.5-flash",
        messages=[{ "content": "Hello, how are you?","role": "user"}]
    )

    print(response)# gemini() function ko call kiya hai, to output kuch is tarah ka JSON-like response hoga — ye response Gemini model ka answer hota hai jo LiteLLM ke completion() function se milta hai.

#     {
#   'id': 'chatcmpl-abc123xyz',
#   'object': 'chat.completion',
#   'created': 1717345678,
#   'model': 'gemini/gemini-1.5-flash',
#   'choices': [
#     {
#       'index': 0,
#       'message': {
#         'role': 'assistant',
#         'content': 'I am good! How can I assist you today?'
#       },
#       'finish_reason': 'stop'
#     }
#   ],
#   'usage': {
#     'prompt_tokens': 10,
#     'completion_tokens': 12,
#     'total_tokens': 22
#   }
# }


def gemini2():
    response = completion(
        model="gemini/gemini-2.0-flash-exp",
        messages=[{ "content": "Hello, how are you?","role": "user"}]
    )

    print(response["choices"][0]["message"]["content"])

gemini()
#openai()   #limit ends of free trials
gemini2()