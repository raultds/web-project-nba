# web-project-nba

This repository contains a python application that shows you the NBA players' and teams' stats from this last seasson.

The players are divided by teams, and the teams by conferences to facilitate the search. 

## How to run it?

Here you have some considerations about how to run the project in your local machine.

### Requisites

This project uses python 3.6 and pip, so you will need to have them both.

With this first step done, you will need to install with pip all the prerequisites in [requirements.txt](https://github.com/raultds/web-project-nba/blob/dev/requirements.txt).

### Running the project

Once you understanded all the requirements, you can clone the repository, and start it with the comand:

$./manage.py runserver

And then, access the web with the delivered link.

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

### Data access

We dispose a little database where we have saved all the players' and teams' names and basic information. And then, we access the [MySportsFeeds](https://www.mysportsfeeds.com/) API to get the last season stats when you select a player/team. 
