from flask import Flask, render_template, request
import string
import random

app = Flask(__name__)

def password_generator(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

@app.route('/', methods=['GET', 'POST'])
def home():
    password = ''
    if request.method == 'POST':
        password = password_generator(int(request.form.get('length')))
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)
