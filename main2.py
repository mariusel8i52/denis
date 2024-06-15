import subprocess
import time
import threading
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'I am alive!'

def run_script():
    while True:
        print("Starting main.py")
        process = subprocess.Popen(['python', 'main.py'])
        process.wait()
        print("main.py stopped. Restarting in 5 seconds...")
        time.sleep(3)
			
def run_flask():
    app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
    script_thread = threading.Thread(target=run_script)
    flask_thread = threading.Thread(target=run_flask)

    script_thread.start()
    flask_thread.start()

    script_thread.join()
    flask_thread.join()