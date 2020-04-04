from flask import Flask, request, url_for, redirect
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.json:
            return 'Got a POST request with a body: %s' % str(request.json)
        else:
            return 'Got a POST request without a body!'
    else:
        import time; time.sleep(2)
        print('getting reloaded!')
        redirect(url_for('index'))
        #return 'index function from a GET request'
