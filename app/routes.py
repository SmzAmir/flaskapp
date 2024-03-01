from app import app


# the index page
@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return "Hello World!"
