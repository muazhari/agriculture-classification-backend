FROM autogluon/autogluon:0.6.1-cuda11.3-framework-ubuntu20.04-py3.8
ENTRYPOINT ["/bin/sh", "-l"]
WORKDIR /repository
COPY . .
RUN apt update -y
RUN apt install -y libpq-dev
RUN pip install -r requirements.txt
RUN pip install pydantic[dotenv]