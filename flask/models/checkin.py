from flask import Blueprint, render_template, request, flash, redirect, url_for
from models.database import engine
from sqlalchemy import text
from datetime import datetime

checkin_bp = Blueprint("checkin", __name__)

@checkin_bp.route("/checkin", methods=["GET", "POST"])
def checkin():
    if request.method == "POST":
        full_name = request.form.get("full_name")
        phone = request.form.get("phone")
        email = request.form.get("email")
        purpose = request.form.get("purpose")

        try:
            with engine.begin() as conn:
                # 1. check if visitor exists
                visitor = conn.execute(
                    text("SELECT id FROM visitor WHERE phone=:phone"),
                    {"phone": phone}
                ).fetchone()

                if visitor:
                    visitor_id = visitor.id
                else:
                    result = conn.execute(
                        text("INSERT INTO visitor (full_name, phone, email) VALUES (:n,:p,:e)"),
                        {"n": full_name, "p": phone, "e": email}
                    )
                    visitor_id = result.lastrowid

                # 2. insert visit with status = IN
                conn.execute(
                    text("INSERT INTO visits (visitor_id, purpose, time_in, status) VALUES (:vid,:pur,:ti,'IN')"),
                    {"vid": visitor_id, "pur": purpose, "ti": datetime.now()}
                )

            flash("✅ Visitor checked in successfully!", "success")
            return redirect(url_for("checkin.checkin"))

        except Exception as e:
            flash(f"❌ Error: {str(e)}", "danger")

    return render_template("checkin.html")
