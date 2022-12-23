# Database System Final Project

## API Requests:

1. Register/Login/Logout (Login before everything)

   * Register:

     ![1](./images/1.png)

   * Login (copy the access_token and paste into all of the following request's header):

     ![2](./images/2.png)

   * Logout:

     ![3](./images/3.png)

2. Customers:

   * List All (put access_token in header required):

     ![4](./images/4.png)

   * Retrieve One Customer (put access_token in header required):

     ![5](./images/5.png)

   * Create a New Customer (put access_token in header required):

     ![6](./images/6.png)

   * Update an Existing Customer (put access_token in header required):

     ![7](./images/7.png)

   * Delete a Customer (put access_token in header required):

     ![8](./images/8.png)

3. Employees:

   * List All (put access_token in header required):

     ![9](./images/9.png)

   * Retrieve One Employee (put access_token in header required):

     ![10](./images/10.png)

   * Create a New Employee (put access_token in header required):

     ![11](./images/11.png)

   * Update an Existing Employee (put access_token in header required):

     ![12](./images/12.png)

   * Delete a Employee (put access_token in header required):

     ![13](./images/13.png)

3. Insurances:

   * List All (put access_token in header required):

     ![14](./images/14.png)

   * Retrieve One Employee (put access_token in header required):

     ![15](./images/15.png)

   * Create a New Employee (put access_token in header required):

     ![16](./images/16.png)

   * Update an Existing Employee (put access_token in header required):

     ![17](./images/17.png)

   * Delete a Employee (put access_token in header required):

     ![18](./images/18.png)
3. Error Messages:
   * When no access_token in header:

     ![19](./images/19.png)

   * When access_token expires:

     ![20](./images/20.png)
## To Run Online

1. This service has been deployed on Render.com
2. Open this link https://db-project.onrender.com/ to access the service
3. Use Postman, GitHub Insomnia, etc to send requests



## To Run Locally
1. Clone this project
2. Open Docker on your computer
3. Open Terminal and use `cd` to get into the current folder
4. In Terminal, type in `docker build -t db-project .` to build the docker image
5. In Terminal, type in `docker run -dp 5000:5000 -w /app -v "$(pwd):/app" db-project sh -c "flask run --host 0.0.0.0` to start the container and app should run in `http://localhost:5000/`.
6. Use Postman, GitHub Insomnia, etc to send requests



## Machine Learning Model
1. The model is avaliable at https://db-project.onrender.com/machine-learning-model if you run online
2. The model is avaliable at `http://localhost:5000//machine-learning-model` if you run locally
3. In case both method failed, the model is avaliable at https://colab.research.google.com/drive/1dgv2vjAvjnUaMrQa_msUfHqF2WjvZ93X?usp=sharing

