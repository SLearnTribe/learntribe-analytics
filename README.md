# Builds
[![Continuos Itegration](https://github.com/SLearnTribe/learntribe-analytics/actions/workflows/Continuos%20Integration.yml/badge.svg)](https://github.com/SLearnTribe/learntribe-analytics/actions/workflows/Continuos%20Integration.yml)
# Flask Application
This is a Flask application that serves as a rest api calls for analytics.

# Requirements
Python >= 3.8

Other dependencies listed in requirements.txt

# Installation
- Clone the repository: git clone https://github.com/SLearnTribe/learntribe-analytics.git
- Navigate to the project directory: cd learntribe-analytics
- Install the required dependencies: pip install -r requirements.txt

# Usage
Run the application:
- python main.py

In postman and navigate to http://localhost:<port_no_specified/<routes>

# Command used for requirements.txt
Dependencies of current project
- python -m pipreqs.pipreqs

Dependencies of current Environment
- pip freeze > requirements.txt

# Docker setup
- docker build -t myapp:latest . 
- docker run -p 8000:8000 myapp:latest

# Docker compose
- docker-compose up -d


# Environment variables
- ISSUER
- KEYCLOAK_PUBLIC_KEY
- CONSUL_URL
