from flask import Flask
from flask import request

app = Flask(__name__)


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.route('/shutdown')
def shutdown():
    shutdown_server()


@app.route('/')
def hello():
    return 'This is the homepage. You can use /shutdown endpoint ' \
           'to crash app or /data to post json data.'


@app.route('/data', methods=['POST'])
def save_data():
    if request.method == 'POST':
        try:
            content_type = request.headers.get('Content-Type')
            if content_type == 'application/json':
                json = request.json
                # write results to file - for testing out volumes in the end
                with open('data/file_with_data.txt', 'a') as f:
                    f.write(str(json)+"\n")
                    return "Written"+str(json)+"to file."
        except:
            return "Writing to file failed"

@app.route('/show')
def show_saved_data():
    with open('data/file_with_data.txt') as f:
        lines = f.read()
        return lines

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)



