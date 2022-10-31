import RPi.GPIO as GPIO            # import RPi.GPIO module  
from time import sleep             # lets us have a delay  
GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD  

from flask import Flask

app = Flask(__name__)

@app.route("/")
def default_page():
  return '''
  <html><head></head><body><h1><a href="/toggle_gate">Toggle Gate</a></h1>
  '''

@app.route("/toggle_gate")
def toggle_gate():
  # with Cayenne installed, we have to share or ignore:
  GPIO.setwarnings(False)
  GPIO_PIN=21
  GPIO.setup(GPIO_PIN, GPIO.OUT)
  GPIO.output(GPIO_PIN, 1)
  sleep(0.5)
  GPIO.output(GPIO_PIN, 0)
  return "<h1>Gate toggled</h1><meta http-equiv='refresh' content='5; url=/'><img src='/static/boom-g1acbb2fd2_640.png'>"

@app.route("/favicon.ico")
def favicon():
  return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/static/<path:path>')
def send_report(path):
    return send_from_directory('static', path)

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)
