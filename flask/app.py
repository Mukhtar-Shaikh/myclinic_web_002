
from flask import Flask,render_template ,jsonify,request

app = Flask(__name__)
clinic_name= "ms"

@app.route("/")

def hello():
    return render_template ("index.html")
    

@app.route("/home")

def home():
   return render_template ("checkin.html")

@app.route("/checkin", methods=["GET", "POST"])
def checkin():
    if request.method == "POST":
        # Process form data here
        full_name = request.form.get("full_name")
        phone = request.form.get("phone")
        email = request.form.get("email")
        employee_id = request.form.get("employee_id")
        purpose = request.form.get("purpose")
        time_in = request.form.get("time_in")

if __name__ == ('__main__'):
    app.run(host= '0.0.0.0' ,debug=True)

