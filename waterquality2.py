import pandas as pd
import numpy as np
from flask import Flask, request, render_template
from sqlalchemy import BigInteger, Column, Float, Integer, Text
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///waterquality.sqlite'
db = SQLAlchemy(app)

df= pd.read_csv('filtered.csv') 

df1 = df[['SchoolCounty','SchoolName','RESULT']]

class WaterQuality(db.Model):
    __tablename__ = 'WaterQuality'
    ID = db.Column(db.Integer, primary_key=True)
    SchoolCounty =db.Column(db.String)
    SchoolName = db.Column(db.String)
    RESULT = db.Column(db.Float)
    
    def __repr__(self):
        return (f"<WaterQuality(SchoolCounty='{self.SchoolCounty}', SchoolName='{self.SchoolName}', RESULT='{self.RESULT}')>")

db.create_all()

for row in df1.itertuples():
    db.session.add(
        WaterQuality(
            SchoolCounty =row.SchoolCounty,
            SchoolName = row.SchoolName,
            RESULT = row.RESULT,
        )
    ) 
         
db.session.commit()

@app.route('/')
def select_county():
    counties={row.SchoolCounty for row in WaterQuality.query.distinct()}
    return render_template('select_county.html',counties=counties)


@app.route('/filter')
def filter_by_county():
    county = request.args.get('county')
    school_filtered =WaterQuality.query.filter_by(SchoolCounty=county)
    
    df_filtered =df1[df1.SchoolCounty==county]
    
    subset = [row.SchoolName for row in school_filtered]
    subset_f=set(subset)
    subset_l=list(subset_f)
    return render_template('show_schools.html', subset=subset_l, county=county)

        

