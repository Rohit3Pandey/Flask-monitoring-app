import psutil
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    cpu_metric = psutil.cpu_percent()
    mem_metric = psutil.virtual_memory().percent

    return render_template('index.html', cpu_metric=cpu_metric, mem_metric=mem_metric)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
