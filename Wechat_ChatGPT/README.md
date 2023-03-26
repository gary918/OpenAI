# Use ChatGPT in Your WeChat Official Account
## Create a WeChat Official Account
## Create a Virtual Machine
* Choose Ubuntu 20.04
* Enable VM to listen at 0.0.0.0:80 by running ```sudo setcap CAP_NET_BIND_SERVICE=+eip /usr/bin/python3.8```
* Set environment variables
```
export OPENAI_API_BASE=https://<YourServiceName>.openai.azure.com/
export OPENAI_API_KEY=<Your API Key>
```
## Connect to OpenAI APIs
* Sign up for OpenAI
* Generate your OpenAI Key
## Connect to Azure OpenAI APIs
* Create Azure OpenAI service