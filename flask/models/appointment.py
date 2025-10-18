from flask import Blueprint, render_template, request, flash, redirect, url_for
from models.database import engine
from sqlalchemy import text
from datetime import datetime
import re

appointment_bp = Blueprint("appointment",__name__)

@appointment_bp.route("/bookAppointment", methods =["GET", "POST"])

def appointment():
    if request.method == "POST":
        full_name = request.form.get(full_name)
        Date_Of_BIrth = request.form.get(Date_Of_BIrth)
        Age = request.form.get(Age)
        doctor = request.form.get(doctor)
        Available_date = request.form.get(Available_date)
        time_slot = request.form.get(time_slot)
        city = request.form.get(city)
        phone_number = request.form.get(phone_number)
        address = request.form.get(address)
        email = request.form.get(email)

      