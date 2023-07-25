FROM python:3.9.13

# Install pylint
RUN pip install --upgrade pip && \
    pip install pylint

# Install git, process tools
RUN apt-get update && apt-get -y install git procps

# Add path for pytest
ENV PYTHONPATH /workspaces/Wechat_ChatGPT/src

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY ./src ./src
CMD ["run"]