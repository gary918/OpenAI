import os
import run_openai
import threading
import werobot
from werobot.replies import TransferCustomerServiceReply

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

def post_wechat_customer_service_reply(messages):
    chatGptResponse = generate_response(messages.content)
    # https://werobot.readthedocs.io/zh_CN/latest/client.html#
    # https://developers.weixin.qq.com/doc/offiaccount/Message_Management/Service_Center_messages.html
    # 获取 Access Token，发送消息的客服账户等API
    return robot.client.send_text_message(user_id=messages.source, content=chatGptResponse, kf_account=None)

@robot.handler
def hello (messages):
    print(messages.content)
    thread = threading.Thread(
        target=post_wechat_customer_service_reply, args=(messages,))
    thread.start()
    # https://developers.weixin.qq.com/doc/offiaccount/Message_Management/Passive_user_reply_message.html
    # 假如服务器无法保证在五秒内处理并回复，必须做出下述回复，这样微信服务器才不会对此作任何处理，
    # 并且不会发起重试（这种情况下，可以使用客服消息接口进行异步回复），否则，将出现严重的错误提示: “该公众号暂时无法提供服务，请稍后再试”
    # 将消息转发至客服:
    # https://developers.weixin.qq.com/doc/offiaccount/Customer_Service/Forwarding_of_messages_to_service_center.html
    return TransferCustomerServiceReply(messages)

robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()