FROM python:3.9

ADD pastebin-bot/bot.py .

RUN pip install -r requriments.txt

CMD ["python", "./bot.py"]