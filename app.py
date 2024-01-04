# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template,jsonify


JOBS = [
  {
    'ID': 1,
    'Title':'Python Developer',
    'Location':'New York',
    'Salary':'$100,000'
  },
  {
    'ID': 1,
    'Title':'Data Analyst',
    'Location':'USA',
    'Salary':'$190,000'
  },
  {
    'ID': 1,
    'Title':'Data Scientist',
    'Location':'UK'
  },
  {
    'ID': 1,
    'Title':'Web Developer',
    'Location':'Germany',
    'Salary':'$195,000'
  },
]
# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
#This is an html route
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return render_template("home.html",jobs=JOBS,company_name='Jovian')
# main driver function



#This is an API route
#RESTAPI, JSONAPI OR API end point looks like this hat means  our info is not only in html form but also in json file
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


#another way to return or access data is using API (JSON) Javascript object
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(host='0.0.0.0',debug=True)