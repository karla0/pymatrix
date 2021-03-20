# used for managing endpoints

@app.route('/')
@app.route('/index')
def index():
    return 'Hello World'