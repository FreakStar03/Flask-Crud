# Flask-Crud

  

**Running a Flask Server/EMV**

	$ mkdir myproject

	$ cd myproject

	$ python3 -m venv NameOfEnv

	$ cp member_data.py /myproject <move  the  .py  file  to  new  created  folder>

	$ source NameOfEnv/bin/activate <activate  the  virtual-environment>

	$ pip3 install dataset

	$ pip3 install Flask

	$ python3 member_data.py

> members_data.py is in Sqlite Folder

  

***Now the venv will run on 5000 port***

|Link  |Method  |Use|
|--|--|--|
|  192.0.0.1:5000/db_populate| Get |To Create The DB(sqilite) file to store data.|
|192.0.0.1:5000/db_clear|Delete|Clear all entries
|192.0.0.1:5000/members|Get|To get json of all entries
|192.0.0.1:5000/members|Post| To add a new entry
|192.0.0.1:5000/members/{id}| Get | TO get  a single member entry by Id
|192.0.0.1:5000/members/{id}|Put | To change the value of a member data by ID
|192.0.0.1:5000/members/{id}|Delete| To delete a member data by id

> The {id} must be replaced by number (1 , 2 ,3 etc)

**Json data Format**

    { 	
    "name": "name_any", 	"password": "password_any", 	
    }



