FROM python:3.9

ADD pastebin-bot/bot.py .

RUN pip install --no-cache-dir --upgrade -r requriments.txt

CMD ["python", "./bot.py"]