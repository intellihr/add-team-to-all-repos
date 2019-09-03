FROM python:3.7.4

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN \
  python -m venv /venv && \
  . /venv/bin/activate && \
  pip install --upgrade pip && \
  pip install \
    --no-cache-dir \
    -r requirements.txt

COPY . .

CMD [ "/usr/src/app/run" ]
