from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import pymysql
import secrets

app = Flask(__name__)

conn = "mysql+pymysql://{0}:{1}@{2}/{3}".format(secrets.dbuser, secrets.dbpass, secrets.dbhost, secrets.dbname)

app.config['SQLALCHEMY_DATABASE_URI'] = conn
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

ma = Marshmallow(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    phone_number = db.Column(db.String(20), unique=True)

    def __init__(self, name, email, phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number

class ContactSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'phone_number')

contact_schema = ContactSchema()
contacts_schema = ContactSchema(many = True)

@app.route('/contact', methods=['GET'])
def get_contacts():
    all_contacts = Contact.query.all()
    result = contacts_schema.dump(all_contacts)
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=True)