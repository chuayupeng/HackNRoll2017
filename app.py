from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

# route for handling the login page logic
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
