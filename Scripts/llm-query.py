
#!/usr/bin/env python3

import os
import sys
import openai

# def main():
#     if len(sys.argv) < 2:
#         sys.exit("Usage: llm-query.py <model_name>")

#     model_name = sys.argv[1]

#     # Pull API key from the environment
#     api_key = os.environ.get("OPENAI_API_KEY")
#     if not api_key:
#         sys.exit("Error: OPENAI_API_KEY is not set")
#     openai.api_key = api_key

#     # Read the full prompt from stdin
#     prompt = sys.stdin.read()

#     # Send a ChatCompletion request
#     response = openai.chat.completions.create(
#         model=model_name,
#         messages=[{"role": "user", "content": prompt}],
#         temperature=0.0
#     )

#     # Print only the assistant’s reply (no extra newline)
#     print(response.choices[0].message.content, end="")

# if __name__ == "__main__":
#     main()


import sys

# from langchain_community.llms import OllamaLLM
# llm_model = Ollama(model=sys.argv[1], temperature=0)

from langchain_ollama import OllamaLLM
llm_model = OllamaLLM(model=sys.argv[1], temperature=0)

prompt = ""

for line in sys.stdin:
  prompt += line

print(llm_model.invoke(prompt))
