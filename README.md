# Process priority tool.

This Django project show how to limit process based on priority.

## Getting Started

You need to install python 3.5 or upper and install virtualenv on your os.

### Installing

Please follow this steps to run the project:

After that, pull this project from GIT and go to project folder

1- Create virtualenv

```
virtualenv myenv
```

2- Active virtualenv

```
source myenv/bin/activate
```

3- Install requirements

```
pip install -r requirements.txt
```

4- Migrate databases

```
python manage.py migrate
```

5- Load sample users

```
python manage.py loaddata users
```

7- Run the project

```
python manage.py runserver 0.0.0.0 8000
```

7- We need to open another console (Terminal) and run this command in project folder:

```
python manage.py start_limiter
```

That's it!

You can use it now.

### How to use & Documentations:

We some sample user you can select them for add new process:

| User ID       | weight        |
| ------------- |:-------------:| 
| 1             | 1             | 
| 2             | 4             |   
| 3             | 1             |
| 4             | 3             |
| 5             | 2             |

For adding new process please call this request to server:

| Method  | URL                                      | data *                            |
| ------- |:----------------------------------------:|---------------------------------|
| POST    | http://0.0.0.0:8000/process/             | user_id : 5 , x : 10            |

This process will import to Queue.

data :

- user id : one of above table user_id (Ex. 3)
- x : Actually is how much time needs to complete task in seconds (Ex. 10)

For get status of tasks you can call this method:

| Method  | URL                                      |
| ------- |:----------------------------------------:|
| GET     | http://0.0.0.0:8000/process/             |

And the console log of start_limiter command you can see what happening in limiter task.

## Developers Guide

You can see what happen in process in this file:

```
limiter/management/commands/start_limiter.py
```

And you can change sleep time to see process better

## Authors

* **Soheil Tayyeb Naeini** - *Initial work* - [StarSoheil2007](https://github.com/starsoheil2007)

## License

This project is licensed under the Free License.

## Acknowledgments

* This is Test for hiring process of one company.

