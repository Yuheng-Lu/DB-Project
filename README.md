## To Run Online
1. This service has been deployed on render.com



## To Run Locally
1. Clone this project
2. Open Docker on your computer
3. Open Terminal and use `cd` to get into the current folder
4. In Terminal, type in `docker build -t db-project .` to build the docker image
5. In Terminal, type in `docker run -dp 5000:5000 -w /app -v "$(pwd):/app" db-project sh -c "flask run --host 0.0.0.0` to start the container and app should run in `http://localhost:5000/`

``docker build -t db-project .``