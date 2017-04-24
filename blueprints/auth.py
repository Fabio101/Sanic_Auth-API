#
# Imports
#

from sanic.blueprints import Blueprint
from sanic.response import json
from sanic_openapi import doc

from lib.logger import *
from lib.auth import *

from models import auth

blueprint = Blueprint('auth', '/auth')

@blueprint.post('/')
@doc.summary('Authenticates a User and Provides JWT Token')
@doc.consumes(auth)
@doc.produces({"token": str})

async def auth(request):
  res = await authenticate().auth(request)
  log.info("received request; HTTP response: "+ str(res[1]))
  return json(res[0], res[1])