from flask import Flask

app = Flask(__name__)
app.secret_key = "secret-sause"

reminders = []

# Sets up global filters for the Jinja2 environment
# @app.template_test('patient')

# Load data into system
# loader = LoadData(system)
# system = loader.Load()