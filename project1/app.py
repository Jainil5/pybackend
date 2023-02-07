import cv2
from flask import *
import requests
app = Flask(__name__,static_url_path="")
camera = cv2.VideoCapture(0)


"""
def generate_frames():
    while True:

        ## read the camera frame
        success, frame = camera.read()
        if not success:
            break
        else:

            img, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
"""

@app.route("/home")
def home():
    return render_template("cam.html")

def generate_frames_home():
    while True:

        ## read the camera frame
        success, frame = camera.read()
        if not success:
            break
        else:
            
            

            img, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_home')
def video_home():
    return Response(generate_frames_home(), mimetype='multipart/x-mixed-replace; boundary=frame')









if __name__ == "__main__":
    app.run(debug=True)
