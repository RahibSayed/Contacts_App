from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import pymysql
import secrets

# Init app
app = Flask(__name__)

# Database
conn = "mysql+pymysql://{0}:{1}@{2}/{3}".format(secrets.dbuser, secrets.dbpass, secrets.dbhost, secrets.dbname)

app.config['SQLALCHEMY_DATABASE_URI'] = conn
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init db
db = SQLAlchemy(app)

# Init ma
ma = Marshmallow(app)

# Contact Model
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    phone_number = db.Column(db.String(20), unique=True)

    def __init__(self, name, email, phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number

# Contact Schema
class ContactSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'phone_number')

# Init Schema
contact_schema = ContactSchema()
contacts_schema = ContactSchema(many = True)

# Get all contacts
@app.route('/contact', methods=['GET'])
def get_contacts():
    all_contacts = Contact.query.all()
    result = contacts_schema.dump(all_contacts)
    return jsonify(result), 200

# Get contact by ID
@app.route('/contact/<id>', methods=['GET'])
def get_contact(id):
    contact = Contact.query.get(id)
    return contact_schema.jsonify(contact), 200

# Get contact by name
@app.route('/contact', methods=['GET'])
def get_contact_by_name():
    name = request.json['name']
    contact = Contact.query.filter(Contact.name.like('%'+ name + '%'))
    return contact_schema.jsonify(contact), 200

# Create contact
@app.route('/contact', methods=['POST'])
def add_contact():
    name = request.json['name']
    email = request.json['email']
    phone_number = request.json['phone_number']
    
    new_contact = Contact(name, email, phone_number)

    db.session.add(new_contact)
    db.session.commit()

    return contact_schema.jsonify(new_contact), 201

# Update contact
@app.route('/contact/<id>', methods=['PUT'])
def update_contact(id):
    contact = Contact.query.get(id)

    name = request.json['name']
    email = request.json['email']
    phone_number = request.json['phone_number']

    contact.name = name
    contact.email = email
    contact.phone_number = phone_number

    db.session.commit()

    return contact_schema.jsonify(contact), 200

# Delete contact
@app.route('/contact/<id>', methods=['DELETE'])
def delete_contact(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()
    return '', 204

# Run Server 
if __name__ == '__main__':
    app.run(debug=True)