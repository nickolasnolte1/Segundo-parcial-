from flask import Flask, request, redirect, url_for, render_template
from jinja2 import Template , Environment, FileSystemLoader


file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)


app = Flask (__name__)

@app.route('/')
def my_form():
    return render_template('formu.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text


if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug = True)