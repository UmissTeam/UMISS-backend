# UMISS-backend
Back end to manage requests and responses to UMISS


## Installation Guide
* Install Python 3.x https://www.python.org/downloads/<br><br>

Install pip3<br>
`$ sudo apt-get install python3-pip`<br><br>


Starting Project<br>
`$ git clone https://github.com/CadeiraCuidadora/UMISS-backend`<br>
`$ cd UMISS-backend/`<br>

Install all python packages<br>
`$ pip3 --user -r requirements.txt`<br><br>

Create tables in db<br>
`$ python3 manage.py migrate`<br>
`$ python3 manage.py runserver`<br>

So, you can acess the network with this url on browser:
`localhost:8000/`

Documentation can be access on:
`localhost:8000/docs`

