
#!/usr/bin/env bash
#
# llm-query.sh → invoke OpenAI via the Python SDK

# 1. Activate your virtualenv (must have `openai` SDK installed)
# source ~/Project/Thesis/llm-td/llm/bin/activate

# # 2. Ensure API key
# if [ -z "$OPENAI_API_KEY" ]; then
#   echo "Error: OPENAI_API_KEY is not set" >&2
#   exit 1
# fi

# # 3. Model name check
# if [ -z "$1" ]; then
#   echo "Usage: $0 <model-name>" >&2
#   exit 1
# fi
# model="$1"

# # 4. Enforce a 300s timeout and dispatch to Python
# perl -e 'alarm shift; exec @ARGV' 300 python3 "$(dirname "$0")/llm-query.py" "$model"









#!/bin/bash

#start python virtual environment to use Ollama framework

source ~/Project/Thesis/llm-td/llm/bin/activate

# run a query to LLM with a timeout of 300 seconds

#gtimeout -v 300 python3 ./llm-query.py $1
perl -e 'alarm shift; exec @ARGV' 300 python3 ./llm-query.py "$1"
