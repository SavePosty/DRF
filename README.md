#Django RSET API

Start:

1. Added .gitignore file https://gist.github.com/LondonAppDev/dd166e24f69db4404102161df02a63ff

https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
https://github.com/LondonAppDev/build-a-backend-api-python-drf-beginner-cheat-sheet/blob/master/README.md

git init
git add .
ssh
push :3 steps provided by github

2. vagrant init ubuntu/bionic64

Replace code: https://gist.github.com/LondonAppDev/199eef145a21587ea866b69d40d28682 
Vagrant up

After downloading:

vagrant ssh

type exit to exit
cd /vagrant : syncing 

3. To run a py file
python filename.py

4. Added updaeded files again
git add .
git commit -m "text"
git push origin

to open vegrant again
vagrant up
vagrant ssh
cd /vagrant

Py env in vagrant
python -m venv ~/env
source ~/env/bin/activate
deactivate : to deactive virtual env

django commands
django-admin.py startproject profiles_project .

. means root here

python manage.py startapp profiels_api

changes to be made in settings.py

INSTALLED_APPS = [
    'profiles_api',
    'rest_framework',
    'rest_framework.authtoken',
]

to run pythondjango server

python manage.py runserver 0.0.0.0:8000

this 8000 is also specified on vargant config

127.0.0.1:8000



Warning : LF will be replaced by CRLF
The term CRLF refers to Carriage Return (ASCII 13, \r ) Line Feed (ASCII 10, \n ). ... For example: in Windows both a CR and LF are required to note the end of a line, whereas in Linux/UNIX a LF is only required.

