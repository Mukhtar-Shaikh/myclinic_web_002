from flask import Blueprint, render_template
from models.database import engine
from sqlalchemy import text

monitor_bp = Blueprint("monitor", __name__)


# visitor history at /visitors
@monitor_bp.route("/visitors", methods=["GET"])
def monitor():
    with engine.connect() as conn:
        # Currently checked-in visitors
        checked_in = conn.execute(
            text("""
                SELECT v.id AS visitor_id, v.full_name, v.phone, vs.purpose, vs.doctor, vs.time_in
                FROM visits vs
                JOIN visitor v ON vs.visitor_id = v.id
                WHERE vs.status='IN'
                ORDER BY vs.time_in ASC
            """)
        ).mappings().all()

        # Visit history (both IN & OUT)
        history = conn.execute(
            text("""
                SELECT v.full_name, v.phone, vs.purpose,vs.doctor, vs.time_in, vs.time_out, vs.status
                FROM visits vs
                JOIN visitor v ON vs.visitor_id = v.id
                ORDER BY vs.time_in DESC
            """)
        ).mappings().all()

    return render_template("monitor.html", checked_in=checked_in, history=history)
