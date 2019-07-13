from flask import Flask, render_template, url_for, request, redirect
from server import app, reminders
from ocr import tessocr
from Reminder import Reminder
import re

@app.route("/", methods=["GET", "POST"])
def home():
    text = ""
    if request.method == "POST":
        file = request.files['filename']
        file_name = file.filename or ''
        destination = '/'.join(["Images/", file_name])
        file.save(destination)
        text = tessocr(destination)
        makeReminder(text)

    return render_template("home.html", text=text)

@app.route("/calendar", methods=["GET", "POST"])
def calendar():
    return render_template("calendar.html", reminders=reminders)

def makeReminder(string):

    rem = Reminder()
    tokens = string.split(" ")
    timePattern = "^\d{2}\:\d{2}\$"
    datePattern = "^\d{1,2}\/\d{1,2}\/\d{4}$"
    for token in tokens:
        print(token)
        # Find dates
        if token == "JAN" or token == "FEB" or token == "MAR" or token == "APR" or token == "MAY" or token == "JUN" or token == "JUL" or token == "AUG" or token == "SEP" or token == "OCT" or token == "NOV" or token == "DEC":
            rem.date = token
            continue
        if re.match(timePattern, token):
            rem.time = token
            continue
        if "UseBy" in string or "Use By" in string:
            print(token)
            temp = token.split('/')
            rem.day = temp[0]
            rem.month = temp[1]
            rem.year = temp[2]
        reminders.append(rem)