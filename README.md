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
pip install -r requirements.txt  # this will install all packages in requirements.txt in our virtual environment

# start django project
django-admin startproject mysite   # mysite is your project name
cd mysite     # go to your project directory

# start django app
python manage.py startapp myapp #myapp is your app name

# makemigrations
python manage.py makemigrations  # anytime you alter or add models makemigrations
python manage.py migrate  # and migrate as well

# create superuser
python manage.py createsuperuser
# run server
python manage.py runserver      #run server
 

