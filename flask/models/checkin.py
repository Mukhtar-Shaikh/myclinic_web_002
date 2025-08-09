
from flask import Blueprint, render_template, request
from models.database import engine
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

checkin_bp = Blueprint("checkin", __name__)

@checkin_bp.route("/checkin", methods=["GET", "POST"])
def checkin():
    if request.method == "POST":
        # Process form data here
        full_name = request.form.get("full_name")
        phone = request.form.get("phone")
        email = request.form.get("email")
        employee_id = request.form.get("employee_id")
        purpose = request.form.get("purpose")
        time_in = request.form.get("time_in")

        with engine.connect() as conn:
            try:
                conn.execute(text("""
                    CREATE TABLE IF NOT EXISTS Checkin (
                        ID INT AUTO_INCREMENT PRIMARY KEY,
                        full_name VARCHAR(200) NOT NULL,
                        phone INT NOT NULL,
                        employee_id INT ,
                        email VARCHAR(100),
                        purpose VARCHAR(300),
                        time_in TIME NOT NULL
                    )
                """))
            
                conn.execute(text("""
                        INSERT INTO Checkin (full_name, phone, employee_id, email, purpose, time_in)
                        VALUES (:full_name, :phone, :employee_id, :email, :purpose, :time_in)
                    """), {
                        "full_name": full_name,
                        "phone": phone,
                        "employee_id": employee_id,
                        "email": email,
                        "purpose": purpose,
                        "time_in": time_in
                    })

                conn.commit()

            except SQLAlchemyError as e:

                print("❌ Database error:", str(e))
            except Exception as e:
                print("❌ Unexpected error:", str(e))

        return render_template("visitor.html",
                               full_name =full_name,phone = phone
                               ,email= email
                                 ,employee_id = employee_id,purpose = purpose
                                 ,time_in = time_in)
    
    return render_template("checkin.html")