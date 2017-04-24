#
# Imports
#

from sanic.blueprints import Blueprint
from sanic.response import json
from sanic_openapi import doc

from lib.logger import *
from lib.register import *
from lib.token import *

from models import register

blueprint = Blueprint('register', '/register')

token = token()

@blueprint.post('/')
@doc.summary('Registers a new User')
@doc.consumes(register)
@doc.produces({"user": str})

async def register(request):

  if await token.verify_token(request):
    res = await registration().register_user(request)
    log.info("received request; HTTP response: "+ str(res[1]))
    return json(res[0], res[1])
  else:
    log.info("received request; HTTP response: 401")
    return json('Unauthorized', 401)