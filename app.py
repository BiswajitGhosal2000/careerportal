from flask import Flask, render_template, jsonify
from database import load_jobs

app = Flask(__name__)


@app.route('/')
def index():
    jobs = load_jobs()
    return render_template('index.html', jobs=jobs, company_name="Rattler")


@app.route('/api/jobs')
def list_jobs():
    jobs = load_jobs()
    return jsonify(jobs)


app.run(host='0.0.0.0', debug=True)
