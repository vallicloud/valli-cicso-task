# Initial Doc for the API service


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