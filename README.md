# django_basics
this is a django basics project
# clone 
clone this repo  to your local machine using the following command: git clone https://github.com/DavisWere/django_basics.git

# create virtual environment 
python -m venv env  # env is your virtual environment

# activate the virtual environment
env\Scripts\activate   # for windows
source env/bin/activate    #for mac and linux

# install packages  
pip install django   # this will install django in our virtual environment

# run the project
django-admin startproject mysite   #mysite is your project name
cd mysite     # go to your project directory
python manage.py startapp myapp #myapp is your app name
python manage.py makemigrations 
python manage.py migrate
python manage.py runserver      #run server
 

