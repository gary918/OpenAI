import os
import run_openai
import werobot
robot = werobot.WeRoBot(token='mytoken') # Your WeChat token filled in Basic Configuration in wechat backend.
run_openai.api_type = "azure"
run_openai.api_version = "2023-03-15-preview"
run_openai.api_base = os.getenv("OPENAI_API_BASE")  # Your Azure OpenAI resource's endpoint value.
run_openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_response(prompt):
    response = run_openai.ChatCompletion.create(
        engine="gpt-35-turbo", # The deployment name you chose when you deployed the ChatGPT or GPT-4 model.
        messages=[
            {"role": "system", "content": "Assistant is a large language model trained by OpenAI."},
            {"role": "user", "content": prompt}
        ]
    )

    message = response['choices'][0]['message']['content']
    return message.strip()

@robot.handler
def hello (messages):
    print(messages.content)
    return generate_response(messages.content)

robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()