FROM ubuntu:18.04

MAINTAINER ribin chalumattu <cribin@inf.ethz.ch>

# This prevents Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# This keeps Python from buffering stdin/stdout
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
    && apt -y install python3 python3-pip
RUN apt -y install libgl1-mesa-glx

# install dependencies
RUN python3 -m pip install --no-cache-dir --upgrade pip

# set work directory
WORKDIR /ferEmotionPredictor

# copy requirements.txt
COPY ./requirements.txt /ferEmotionPredictor/requirements.txt

# install project requirements
RUN pip install -r requirements.txt

# copy project
COPY . .

# set app port
EXPOSE 5007

ENTRYPOINT ["gunicorn", "--config", "gunicorn_config.py", "--env", "API_CONFIG=api_config.json", "aesthetics_predictor_api_pkg.predictor_api_server:app"]