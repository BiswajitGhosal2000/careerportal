from flask import Flask, render_template, jsonify

app = Flask(__name__)

jobs = [
    {
        "id": 1,
        "title": "Data Scientist",
        "location": "Bengaluru",
        "salary": "$1000"
    },
    {
        "id": 2,
        "title": "Data Analyst",
        "location": "Pune",
        "salary": "$11000"
    },
    {
        "id": 3,
        "title": "DevOps Engineer",
        "location": "Delhi",
        "salary": "$10000"
    },
    {
        "id": 4,
        "title": "UI/UX Designer",
        "location": "Ahmedabad",
        "salary": "$2000"
    },
    {
        "id": 5,
        "title": "Marketing Manager",
        "location": "Hyderabad",
        "salary": "$7000"
    },
    {
        "id": 6,
        "title": "DevOps Engineer",
        "location": "Hyderabad",
        "salary": "$2000"
    },
    {
        "id": 7,
        "title": "DevOps Engineer",
        "location": "Chennai",
        "salary": "$4000"
    },
    {
        "id": 8,
        "title": "Marketing Manager",
        "location": "Kolkata",
        "salary": "$3000"
    },
    {
        "id": 9,
        "title": "Business Analyst",
        "location": "Ahmedabad",
        "salary": "$9000"
    },
    {
        "id": 10,
        "title": "DevOps Engineer",
        "location": "Mumbai",
        "salary": "$8000"
    },
    {
        "id": 11,
        "title": "Machine Learning Engineer",
        "location": "Ahmedabad",
        "salary": "$9000"
    }
]


@app.route('/')
def index():
    return render_template('index.html', jobs=jobs, company_name="Rattler")


@app.route('/api/jobs')
def list_jobs():
    return jsonify(jobs)


app.run(host='0.0.0.0', debug=True)
