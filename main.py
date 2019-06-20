from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin:10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action= "encrypt">
            <label for= "rot">Rotate by:</label>
            <input type="text" name="rot" />
            <textarea name="text"></textarea>
            <input type= "submit" />
        </form>
    </body>
</html>
"""

@app.route("/", methods=['POST', 'GET'])
def index():
    return form

@app.route("/encrypt", methods=['POST', 'GET'])
def encrypt():
    user_rot = request.args.get('rot')
    user_text = request.args.get('text')
    crypto = rotate_string(user_text, user_rot)
    return "<h1>" + crypto + "</h1>"

app.run()