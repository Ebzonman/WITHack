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
        return redirect(url_for("upload", filename=file_name))
    return render_template("home.html", text=text)

@app.route("/calendar", methods=["GET", "POST"])
def calendar():
    return render_template("calendar.html", reminders=reminders)

@app.route("/upload/<filename>", methods=["GET", "POST"])
def upload(filename):
    destination = '/'.join(["Images", filename])
    print(destination)
    text = tessocr(destination)
    if request.method == "POST":
        makeReminder(text)
        return redirect(url_for("calendar"))
    return render_template("upload.html", text=text)

def monthToNum(shortMonth):
    return{
        "1":'Jan',
        "2":'Feb',
        "3":'Mar',
        "4":'Apr',
        "5":'May',
        "6":'Jun',
        "7":'Jul',
        "8":'Aug',
        "9":'Sep', 
        "10":'Oct',
        "11":'Nov',
        "12":'Dec'
}[shortMonth]

def makeReminder(string):

    rem = Reminder()
    tokens = string.split(" ")
    if len(tokens) == 1:
        date = tokens[0].split(":")
        date = date[1].split("/")
        rem.date = date[0]
        rem.month = date[1]
        rem.year = date[2]
    elif len(tokens) == 2:
        rem.name = tokens[1].title()
        date = tokens[1].split(":")
        date = date[1].split("/")
        rem.date = date[0]
        rem.month = date[1]
        rem.year = date[2]
    elif len(tokens) == 3:
        rem.name = tokens[1].title()
        date = tokens[1].split(":")
        date = date[1].split("/")
        rem.date = date[0]
        rem.month = date[1]
        rem.year = date[2]
        rem.time = tokens[2]
    rem.month = monthToNum(rem.month)
    reminders.append(rem)