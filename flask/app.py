
from flask import Flask,render_template ,jsonify,request
from models.checkin import checkin_bp
from models.checkout import checkout_bp
from models.monitor import monitor_bp
from models.database import engine 


app = Flask(__name__)
app.secret_key = "super-secret-key-change-me" 

clinic_name= "ms"

@app.route("/dashboard")

def hello():
    return render_template ("index.html")
    
app.register_blueprint(checkin_bp)
app.register_blueprint(checkout_bp) 
app.register_blueprint(monitor_bp)

@app.route("/book%20appointment")
def home():
   return render_template ("bookapp.html")

if __name__ == '__main__':
    app.run(host= '0.0.0.0' ,debug=True)

