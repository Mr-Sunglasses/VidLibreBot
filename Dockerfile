FROM python:3.9

WORKDIR /code

COPY ./reverse_requirement.txt /code/reverse_requirement.txt

RUN pip install --no-cache-dir --upgrade -r /code/reverse_requirement.txt

COPY ./pastebin-bot /code/pastebin-bot

CMD ["python", "/code/pastebin-bot/bot.py"]
