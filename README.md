# Initial Doc for the API service

## Design Considerations

1. Webapp service: Used Python simple webapp framework called "Flask" to create the API webservice app. Currently it serves only couple of API's and can be implemented fulfledged at later time

2. Database: Used Falsk-SQlAlchemy for creating database for sample data of Malware URLs. The data is stored in simple format of id, url and status. 

Currently no auth modules are included but auth can be added using sessions and cookies from jwt python library.

## Setup Instructions

Pre-req: Make sure python is installed. Below commands are validated in windows

1. Setup a python virtual env and Install required libs 

> pip install virtualenv
> virtualenv env1
> . env1/Scripts/activate
>    pip install -U Flask Flask-SQLAlchemy

2. Setuo sample database entries 
> python db_setup.py

3. Start the web app 

> python main.py

Once webapp starts successfully, you can access it at localhost:9000 