from flask import Flask, request

app = Flask(__name__)

# SET FALSE BEFORE PRODUCTION
if __name__ == "__main__":
    app.run(debug=True)
