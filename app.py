#
# Imports
#

from sanic import Sanic
from sanic_cors import CORS, cross_origin
from sanic_openapi import swagger_blueprint, openapi_blueprint
from blueprints.auth import blueprint as auth_blueprint
from blueprints.register import blueprint as register_blueprint

##################################################
#                                                #
# Description: Main Sanic application            #
#                                                #
##################################################

app = Sanic()
CORS(app)

app.blueprint(openapi_blueprint)
app.blueprint(swagger_blueprint)
app.blueprint(auth_blueprint)
app.blueprint(register_blueprint)


app.config.API_VERSION = '0.0.1'
app.config.API_TITLE = 'Sanic REST API'
app.config.API_DESCRIPTION = 'General REST API with Basic Authentication FUnctions'
app.config.API_TERMS_OF_SERVICE = 'With great power comes great responsibility!'
app.config.API_PRODUCES_CONTENT_TYPES = ['application/json']
app.config.API_CONTACT_EMAIL = 'fabio@mandelbrot.co.za'

#
# Description: Run the Sanic server
#

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8000)