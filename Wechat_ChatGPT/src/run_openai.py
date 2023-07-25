import os
import openai
import json

# Load config values
with open(r'config.json') as config_file:
    config_details = json.load(config_file)
    
# Setting up the deployment name
chatgpt_model_name = config_details['CHATGPT_MODEL']

# This is set to `azure`
openai.api_type = "azure"

# The API key for your Azure OpenAI resource.
openai.api_key = config_details['OPENAI_API_KEY']

# The base URL for your Azure OpenAI resource. e.g. "https://<your resource name>.openai.azure.com"
openai.api_base = config_details['OPENAI_API_BASE']

# Currently Chat Completion API have the following versions available: 2023-03-15-preview
openai.api_version = config_details['OPENAI_API_VERSION']

try:
    response = openai.ChatCompletion.create(
                  engine=chatgpt_model_name,
                  messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": "Who won the world series in 2020?"}
                    ]
                )

    # print the response
    print(response['choices'][0]['message']['content'])
    
except openai.error.APIError as e:
    # Handle API error here, e.g. retry or log
    print(f"OpenAI API returned an API Error: {e}")

except openai.error.AuthenticationError as e:
    # Handle Authentication error here, e.g. invalid API key
    print(f"OpenAI API returned an Authentication Error: {e}")

except openai.error.APIConnectionError as e:
    # Handle connection error here
    print(f"Failed to connect to OpenAI API: {e}")

except openai.error.InvalidRequestError as e:
    # Handle connection error here
    print(f"Invalid Request Error: {e}")

except openai.error.RateLimitError as e:
    # Handle rate limit error
    print(f"OpenAI API request exceeded rate limit: {e}")

except openai.error.ServiceUnavailableError as e:
    # Handle Service Unavailable error
    print(f"Service Unavailable: {e}")

except openai.error.Timeout as e:
    # Handle request timeout
    print(f"Request timed out: {e}")
    
except:
    # Handles all other exceptions
    print("An exception has occured.")