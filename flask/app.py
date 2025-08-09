
from flask import Flask,render_template ,jsonify,request
from models.checkin import checkin_bp

from models.database import engine 


app = Flask(__name__)

clinic_name= "ms"

@app.route("/")

def hello():
    return render_template ("index.html")
    
app.register_blueprint(checkin_bp)

@app.route("/ms")
def home():
   return render_template ("bookapp.html")

if __name__ == '__main__':
    app.run(host= '0.0.0.0' ,debug=True)

