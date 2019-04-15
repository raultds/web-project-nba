# web-project-nba

This repository contains a python application that shows you the NBA players' and teams' stats from this last seasson.

The players are divided by teams, and the teams by conferences to facilitate the search.

## Authors

- Arnau Nadal

- Raul Roca

- Pablo Serrano

- Francesc Tuset

## How to run it?

Here you have some considerations about how to run the project in your local machine.

### Localy
  ## Requisites

  This project uses python 3.6 and pip, so you will need to have them both.

  With this first step done, you will need to install with pip all the prerequisites in [requirements.txt](https://github.com/raultds/web-project-nba/blob/dev/requirements.txt).

  ## Running the project

  Once you understood all the requirements, you can clone the repository, and start it with the comand:

  $./manage.py runserver

  And then, access the web with the delivered link. The users and the passwords to acces are the next ones:

  ### As a User

  Username: prova

  Password: nba123456789

  ### As an Admin

  Username: admin

  Password: nbastats1234

### Deployed
  We deployed our application to Heroku. After more than 30 tries, we managed to deploy the application to heroku but the static images   are not properly shown. You can acces the conference links if you click to the "missing image" icon. On the next deliverable it will     be solved. 
  Link: https://nbastats.herokuapp.com/

## Design decisions

### 12 factor guidelines

We decided to follow the 12 factor guidelines as much as possible in our project fulfilling the next guidelines:

#### - Codebase

One codebase tracked in revision control, many deploys.

#### - Dependencies

Explicitly declare and isolate dependencies.

#### - Config

Store config in the environment.

#### - Build, release, run

Strictly separate build and run stages (In this case, it's more like an objective than an accomplishment. Our design meet its, but heroku is not working well yet in our project, so until we fix the errors it will be pending).

### Models

We have created 3 different models, which are conference', team' and 'player'. This is, also, the distribution that we have done with the information.

### Data access

We dispose a little database where we have saved all the players' and teams' names and basic information. And then, we access the [MySportsFeeds](https://www.mysportsfeeds.com/) API through a separate python function to get the last season stats when you select a player/team. 
