# flask mnist

Flask application that classifies MNIST images.  Images can be obtained from [here](https://www.kaggle.com/scolianni/mnistasjpg#img_103.jpg).  

Flask web application code and frontend largely based on this [repo](https://github.com/avinassh/pytorch-flask-api-heroku).

Model training code can be found in this [repo](https://github.com/celis/mnist).

## Requirements

Create a virtual enviroment and install the requirements with:

    pip install -r requirements.txt

## Deployment

The project is currently deployed in Heroku.  
Needs to set the required configuration variables in Heroku.

In order to run locally adjust the config files and run:

    python app.py
