from flask import Flask, render_template, url_for, request, redirect
from server import app, reminders

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")

@app.route("/calendar", methods=["GET", "POST"])
def calendar():
    return render_template("calendar.html", reminders=reminders)