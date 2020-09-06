Docker related files are written manually. They tell what dependecies
our app needs and how to install them aswell as our app.
The files are: requirements.txt, Dockerfile and docker-compose.yml

---------------------- How to use this ----------------------

Download and install docker for your machine. (google to find it)
If the process asks you to update something just do it. Its very simple and fast anyway.

Download or clone this project.

If you clone give command after cloning:
rm -rf .git (to remove git reference to my repo.)

Then give command: docker-compose build
Then give command: docker-compose up

This should download needed images, create and start container.

then in your browser http://127.0.0.1:8000/ should show the html page.

open another bash/terminal to say: docker-compose down (the first bash is locked while container is running)

++
More advanced docker setup is here: https://github.com/Point-SimoSiren/recipe-api-docker-django-rest
There is also postgres configured to run in docker and unit tests for all functionalities however
the app itself may not be ready yet.

