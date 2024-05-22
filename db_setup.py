# Importing all database and table definitions from primary "app.py" 
import app 
from app import * 

with app.app_context():
    # Create the database and the database table
    db.create_all()

    # Insert the data
    db.session.add(MalwareURL("cisco.com", "GOOD"))
    db.session.add(MalwareURL("test.com", "BAD"))
    db.session.add(MalwareURL("amazon.com", "GOOD"))
    db.session.add(MalwareURL("malware.com", "BAD"))
    db.session.add(MalwareURL("auth.accept", "GOOD"))
    db.session.add(MalwareURL("valli.reject", "BAD"))
    # Format to add further data points: db.session.add(MalwareURL("url", "status"))

    # Commit the changes
    db.session.commit()
