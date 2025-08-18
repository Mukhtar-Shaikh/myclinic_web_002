from flask import Blueprint, render_template, request, flash, redirect, url_for
from models.database import engine
from sqlalchemy import text
from datetime import datetime

checkout_bp = Blueprint("checkout", __name__)

@checkout_bp.route("/checkout", methods=["GET", "POST"])
def checkout():
    if request.method == "POST":
        visitor_id = request.form.get("visitor_id")

        try:
            with engine.begin() as conn:
                # find latest IN visit
                visit = conn.execute(
                    text("SELECT id FROM visits WHERE visitor_id=:vid AND status='IN' ORDER BY time_in DESC LIMIT 1"),
                    {"vid": visitor_id}
                ).fetchone()

                if not visit:
                    flash("❌ No active visit found.", "danger")
                else:
                    # mark OUT
                    conn.execute(
                        text("UPDATE visits SET status='OUT', time_out=:t WHERE id=:id"),
                        {"id": visit.id, "t": datetime.now()}
                    )
                    flash("✅ Visitor checked out successfully!", "success")

        except Exception as e:
            flash(f"❌ Error: {str(e)}", "danger")

        return redirect(url_for("checkout.checkout"))

    # list active visits
    with engine.connect() as conn:
        checked_in = conn.execute(
            text("""
                SELECT v.id AS visitor_id, v.full_name, v.phone, vs.purpose, vs.time_in
                FROM visits vs
                JOIN visitor v ON vs.visitor_id = v.id
                WHERE vs.status='IN'
                ORDER BY vs.time_in ASC
            """)
        ).mappings().all()

    return render_template("checkout.html", checked_in=checked_in)
