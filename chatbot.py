import os
from llama_index.llms.gemini import Gemini
from llama_index.core.llms import ChatMessage
from dotenv import load_dotenv

#   Import libraries here
#
#   Refer to https://docs.llamaindex.ai/en/stable/examples/llm/gemini/ for help
#

load_dotenv()

# Write code to create a chatbot

llm = Gemini(
    model="models/gemini-1.5-flash",

)

# messages = []

all_stuff = "System: You are to answer in brief, conversation-like answers.\n"
while True:
    i = input("Msg: ")
    if i == 'q':
        break
    
    all_stuff += f"User: {i}\n"
    response = llm.complete(all_stuff)
    print(response)
    all_stuff += f"Agent: {response}\n"
