# CPSC-61200-004-Week5

## Cloning this project
To make a clone of this project, you can clone using git from a terminal with the following command:
```
$ git clone https://github.com/elijahmolloy/CPSC-61200-004-Week5.git
```

If that command does not work, a .zip of the project can be downloaded from the [PROJECT URL](https://github.com/elijahmolloy/CPSC-61200-004-Week5).

## Project Structure

The project directory is made up of the following main pieces
```
- myapp
    - templates
        - index.html
    - urls.py
    - views.py
- weekFive
    - settings.py
    - urls.py
- manage.py
- README.md
```

### manage.py
The ```manage.py``` file contains methods that can be used to interact with this project from the command line/terminal. There were really only a few commands that were used during the construction of this project, which include:

1. To actually launch the server for viewing at the [LOCAL SERVER URL](http://127.0.0.1:8000/):
```
$ python manage.py runserver
```
2. To migrate to updated django pieces. This should not prevent from the launching of this project locally, but was recommended when I first launched this project locally. If an error with this recomendation is outputted when first launching, this may be a good idea:
```
$ python manage.py migrate
```
3. To create an app within the project. Apps are essentailly sub-modules of a project. I believe that all views should be contained within an app, but there can be multiple apps within a single project:
```
$ python manage.py startapp myapp
```

### myapp
This app consists of a single view which displays ```Hello World!``` to users after  navigating to the [LOCAL SERVER URL](http://127.0.0.1:8000/).
- ```urls.py``` is a file that was not included in the out-of-the-box app, but was created to store all urls that were setup as part of this app
- ```templates.index.html``` is a view template that is used for the hello world view displayed to users
- ```views.py``` is the function based view responsible for linking the index.html view file and the actual url/path where that template should be viewed at. It also passed variabels to the screen for usage in the index.html file.

### weekFive
The project consists of a single app (ref ```myapp```) as well as all of the out-of-the-box project pieces that are generated when creating a new django project. 
- ```settings.py``` is where we can reference the app we created after the project
- ```urls.py``` is where we can import all urls that were created under the ```myapp``` directory 

## Running this Project
After getting a copy of this repository locally, there is one main command to get everything up and running:

```
$ python manage.py runserver 
```

This is under the assumption that python has been downloaded and is able to be run. This command will launch the server and can be interacted with using the [LOCAL SERVER URL](http://127.0.0.1:8000/).
