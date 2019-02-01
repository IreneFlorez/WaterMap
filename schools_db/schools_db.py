import pandas as pd
from flask import Flask
from sqlalchemy import BigInteger, Column, Float, Integer, Text
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schools.db'
db = SQLAlchemy(app)

df_schools= pd.read_csv('pubschls.txt', sep="\t")

class School(db.Model):
    __tablename__ = 'schools'

    id = db.Column(db.Integer, primary_key=True)
    cds_code_id = db.Column(db.String)
    nces_dist_id = db.Column(db.String)
    nces_school_id = db.Column(db.String)
    status = db.Column(db.String)
    county = db.Column(db.String)
    district = db.Column(db.String)
    school = db.Column(db.String)
    street = db.Column(db.String)
    city = db.Column(db.String)
    zip = db.Column(db.String)
    state = db.Column(db.String)
    address = db.Column(db.String)
    phone = db.Column(db.String)
    web = db.Column(db.String)
    admin_first_name = db.Column(db.String)
    admin_last_name = db.Column(db.String)
    admin_email = db.Column(db.String)
    last_update = db.Column(db.String)

# Uncomment below if db needs to be recreated
# db.drop_all()
# db.create_all()

# for row in range(len(df_schools[:-1])):
#     s = df_schools.loc[row,:].values.tolist()
#     db.session.add(
#             School(
#                 cds_code_id = s[0],
#                 nces_dist_id = s[1],
#                 nces_school_id = s[2],
#                 status = s[3],
#                 county = s[4],
#                 district = s[5],
#                 school = s[6],
#                 street = s[7],
#                 city = s[9],
#                 zip = s[10],
#                 state = s[11],
#                 address = s[12],
#                 phone = s[17],
#                 web = s[19],
#                 admin_first_name = s[39],
#                 admin_last_name = s[40],
#                 admin_email = s[41],
#                 last_update = s[48]
#             )
#         )

# db.session.commit()