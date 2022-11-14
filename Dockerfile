FROM python:3.9

WORKDIR /code

COPY ./requriments.txt /code/requriments.txt

RUN pip install --no-cache-dir --upgrade -r /code/requriments.txt

COPY ./pastebin-bot /code/pastebin-bot

CMD ["python", "/code/pastebin-bot/bot.py"]
