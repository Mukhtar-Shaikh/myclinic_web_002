from flask import Blueprint, render_template, request, flash, redirect, url_for
from models.database import engine
from sqlalchemy import text
from datetime import datetime
import re

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/dashboard")
def dashboard():
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


        history = conn.execute(
            text("""
                SELECT v.full_name, v.phone, vs.purpose, vs.doctor, vs.time_in, vs.time_out, vs.status
                FROM visits vs
                JOIN visitor v ON vs.visitor_id = v.id
                ORDER BY vs.time_in DESC
            """)
        ).mappings().all()

    return render_template("index.html", checked_in=checked_in, history=history)