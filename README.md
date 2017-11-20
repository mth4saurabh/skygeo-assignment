# Full-Stack Developer Test Solution

This README explains how to setup REST API (django) and Single page application / Front-end (React) on local

Note that both project are deployed on heroku:

* [API](https://skygeo-assignment1.herokuapp.com/api-auth/login/?next=/) - Please login using following credentials
	```
	Username: skygeo
	Password: skygeo2017
	```
* [Web App](http://skygeo-assignment2.herokuapp.com/) - Front end displaying all the data provided with the assignment, one can filter through data using search functionality on top

## Getting Started

* Folder `assignment/` contains SQL data and some PHP application code for reference. 
* Folder `assignment1/django/` contains REST API build with django (using Django rest framework)
* Folder `assignment2/client/` contains single page application (using React) as Front-End to consume API built in assignment 1

### Prerequisites

* Pip
* Virtualenv
* Python 2.7
	* Django
	* Django rest framework
* Node, npm for React dependencies

## Installing

A step by step series of examples that tell you have to get a development env running for both parts of assignment


### 1. API in Django

Create a virtualenv to isolate our package dependencies locally:
```
virtualenv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

Install all the project dependencies:
```
cd assignment1/django
pip install -r requirments.txt
```

Now sync your database for the first time and also create superuser. For consistency please use `username: skygeo` and `password: skygeo2017`	
```
python manage.py migrate
python manage.py createsuperuser
```

Start server from command line (default port 8000):
```
python manage.py runserver
```

### 2. Front end in react

Let's dive into client folder:
```
cd assignment2/client
```

Make sure you have all the dependencies install using `npm install`


```
// assignment2/client/package.json
{
	"name": "client",
	"version": "0.1.0",
	"private": true,
	"dependencies": {
	"bootstrap": "^4.0.0-beta",
	"react": "^16.1.1",
	"react-dom": "^16.1.1",
	"react-scripts": "1.0.17",
	"reactstrap": "^5.0.0-alpha.3"
},
"scripts": {
	"start": "react-scripts start",
	"build": "react-scripts build",
	"test": "react-scripts test --env=jsdom",
	"eject": "react-scripts eject"
	}
}
```

If superuser created in API doesn't have following credentials, you'll need to update Authorization in `assignment2/client/src/App.js`

```
username: skygeo
password: skygeo2017
```

Run client side from command line (default port 3000):
```
npm run start
```


## Built With

* [Django REST framework](http://www.django-rest-framework.org/) - The framework used for building API
* [React](https://reactjs.org/) - Used for building frontend 
* [Heroku](https://www.heroku.com/) - Used for staging both the applications above.

## Caveats

* For sake for simplicity & non complexity of the project I have skipped testing as it would involve running basic(copied) templates and won't reflect skills I want to show as full stack developer.
* API documentation could be improved with third party packeges like [Swagger](https://swagger.io/).
* I have also skipped API versioning which would be essential in real world scenario but can be skipped here. 

## Authors

* **Saurabh B**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
