import time, socket
from flask import Flask, render_template, request
import webbrowser

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('map.html')

@app.route('/camera_preview')
def camera_preview():
    cam_id = request.args.get('id')
    return render_template('index.html', cam_id=cam_id)
# open in browser
def open_in_browser():
    time.sleep(2)
    ip_address = socket.gethostbyname(socket.gethostname())
    port = 5000
    local_ip = f"http://{ip_address}:{port}"
    webbrowser.open(local_ip)

if __name__ == '__main__':
    open_in_browser()
    app.run(host='0.0.0.0', port=5000, debug=True)


