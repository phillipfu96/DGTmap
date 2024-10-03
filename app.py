#from flask import Flask, render_template
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/map')
def index():
    return render_template('map.html')

@app.route('/camera_preview')
def camera_preview():
    cam_id = request.args.get('id')
    return render_template('index.html', cam_id=cam_id)



if __name__ == '__main__':
    app.run(debug=True)

