from flask import Flask, render_template, jsonify, request, redirect, url_for, session, flash
import secrets
from flask_bcrypt import Bcrypt
from database import load_jobs, get_job_by_id, apply_job, sign_in, get_applications_by_job_id

app = Flask(__name__)

app.secret = "secret"
bcrypt = Bcrypt()

print(secrets.token_hex(16))


@app.route('/')
def index():
    jobs = load_jobs()
    return render_template('index.html', jobs=jobs, company_name="Rattler")


# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        hashed_password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
        user = User(username=request.form['username'], email=request.form['email'], password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')


# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email']).first()
        if user and bcrypt.check_password_hash(user.password, request.form['password']):
            # Login successful
            return redirect(url_for('index'))
        else:
            # Login failed
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html')


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


@app.route('/applications/<jobid>')
def applications(jobid):
    all_applications = get_applications_by_job_id(jobid)
    return jsonify(all_applications)


app.run(host="0.0.0.0", debug=True)
