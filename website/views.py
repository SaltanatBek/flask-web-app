from flask import Blueprint, render_template, request, flash, redirect
from .models import Discover, Disease, DiseaseType, Discover
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    
    disease_code = request.form.get('disease_code')
    pathogen = request.form.get('pathogen')
    description = request.form.get('description')
    id = request.form.get('id')
    first_enc_date = request.form.get('first_enc_date')
    cname = request.form.get('cname')
    if disease_code or pathogen or description or id or first_enc_date or cname:
        disease = db.session.query(Disease, Discover).join(Disease, Discover.disease_code == Disease.disease_code).filter(Discover.disease_code == Disease.disease_code)
        if disease_code:
            disease = disease.filter_by(disease_code=disease_code)
        if pathogen:
            disease = disease.filter_by(pathogen=pathogen)
        if description:
            disease = disease.filter_by(description=description)
        if id:
            disease = disease.filter_by(id=id)
        print(disease.all())
        if len(disease.all())==0:
            flash('Please, fill all required fields', category='error')
    else: 
        disease = []
    
    
    diseases = db.session.query(Disease, Discover).join(Disease, Discover.disease_code == Disease.disease_code).filter(Discover.disease_code == Disease.disease_code).all()
    
    return render_template("home.html", disease=disease, diseases=diseases)
       
    

