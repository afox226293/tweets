from run_stream import start_stream
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "running"


if __name__ == '__main__':
    start_stream(['Trump'])
    app.run(debug=True)
