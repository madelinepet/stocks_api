# Stocks API
An application that allows a user to create a stocks portfolio in a db, based on information from a 3rd party API.

## Getting started
Clone the repo, run "pipenv shell" in your command line. "pipenv install", "pserve development.ini --reload" to start server, make calls to the routes in an app like Postman or using HTTPy. ALSO, look in the README.txt, it's helpful


## Author
Madeline Peters

## Routes
/

api/v1/company/{symbol}/
Example: http://localhost:6543/api/v1/company/msft/

api/v1/portfolio/{symbol}/
Example: http://localhost:6543/api/v1/portfolio/msft/


api/v1/stock
