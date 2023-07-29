from flask import Flask, jsonify

app = Flask(__name__)

# Sample data
modules_list = ["Module 1", "Module 2", "Module 3"]
user_info = {
    "PRN": "123456789",
    "Name": "John Doe",
    "Phone": "123-456-7890"
}

@app.route('/')
def index():
    return "Welcome to ITIL exam"

@app.route('/modules')
def get_modules():
    return jsonify(modules_list)

@app.route('/me')
def get_user_info():
    return jsonify(user_info)

if __name__ == '__main__':
    app.run()

