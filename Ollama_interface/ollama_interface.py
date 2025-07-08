# Step 1: Import required libraries
import subprocess
import re
import pandas as pd

# Step 2: Load GTFS data from your actual .txt files
calendar = pd.read_csv('data/calendar.txt')
trips = pd.read_csv('data/trips.txt')
stop_times = pd.read_csv('data/stop_times.txt')

# Step 3: Function to send prompt to Ollama (Mistral model)
def ask_ollama(prompt):
    system_instructions = """
You are a transit data assistant. Respond ONLY with a valid Python code block using pandas.
Assume GTFS data is loaded in variables: calendar, trips, stop_times.
"""
    full_prompt = system_instructions + "\n" + prompt
    result = subprocess.run(
        ['ollama', 'run', 'mistral'],
        input=full_prompt.encode(),
        capture_output=True
    )
    return result.stdout.decode()

# Step 4: Extract Python code block and execute it
def execute_response_code(response):
    code_match = re.search(r"```python(.*?)```", response, re.DOTALL)
    if code_match:
        code = code_match.group(1)
        print("💻 Executing code:\n", code)
        try:
            exec(code, globals())
        except Exception as e:
            print("❌ Error while executing code:", e)
    else:
        print("❌ No Python code block found.")

# Step 5: Ask your GenAI-powered question
response = ask_ollama("Which routes operate after 8 PM on Sundays?")
execute_response_code(response)
