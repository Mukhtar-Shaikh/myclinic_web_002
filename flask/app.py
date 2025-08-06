
from flask import Flask,render_template ,jsonify

app = Flask(__name__)
clinic_name= "ms"

@app.route("/")

def hello():
    return render_template ("index.html")
    

@app.route("/home/")

def home():
   return render_template ("Doctors.html")

if __name__ == ('__main__'):
    app.run(host= '0.0.0.0' ,debug=True)

