import openai

# Set up authentication
openai.api_key = "TOKEN_KEY"

# Define the prompt
prompt = input("Enter a prompt: ")

# Define the request payload
request = {
    "model": "text-davinci-002",
    "prompt": prompt,
    "temperature": 0.5,
    "max_tokens": 500,
    "stop": "\n",
}

# Send the request to the API
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    temperature=0.5,
    max_tokens=50,
    n=1,
    stop=None,
    timeout=300,
)


# Print the response or an error message if the response was empty
if len(response.choices) > 0:
    generated_text = response.choices[0].text.strip()
    print(f"Generated text: {generated_text}")
else:
    print("Error: Empty response from API")
