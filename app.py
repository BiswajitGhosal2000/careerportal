from flask import Flask, render_template, jsonify, request

import database
from database import load_jobs, get_job_by_id, apply_job

app = Flask(__name__)


@app.route('/')
def index():
    jobs = load_jobs()
    return render_template('index.html', jobs=jobs, company_name="Rattler")


@app.route('/api/jobs')
def list_jobs():
    jobs = load_jobs()
    for job in jobs:
        job["_id"] = str(job["_id"])
    return jsonify(jobs)


@app.route('/job/<jobid>')
def job_by_id(jobid):
    job = get_job_by_id(jobid)
    if not job:
        return "Not Found", 404
    return render_template('jobpage.html', job=job)


@app.route('/job/<jobid>/apply')
def apply(jobid):
    alert = apply_job(jobid, request.args)
    jobs = load_jobs()
    return render_template('index.html', jobs=jobs, alert=alert)


app.run(host="0.0.0.0", debug=True)
