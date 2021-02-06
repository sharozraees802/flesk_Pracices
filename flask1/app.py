from flask import Flask, render_template, url_for

app = Flask(__name__)


# @app.route('/')
# def index():
#     return "Hello World"


# client = pymongo.MongoClient("mongodb://user:user@<hostname>/<dbname>?ssl=true&replicaSet=atlas-dvw7zq-shard-0&authSource=admin&retryWrites=true&w=majority")
# db = client.test
# mongodb+srv://user:user@cluster0.7ottc.mongodb.net/todeappflask?retryWrites=true&w=majority

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sharoz')
def sharoz():
    return "Hello sharoz"


if __name__ == "__main__":
    app.run(debug=True)
