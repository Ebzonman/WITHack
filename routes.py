from flask import Flask, render_template, url_for, request, redirect
from server import app #, system

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")