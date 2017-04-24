#
# Imports
#

import os
import jwt
import yaml
from datetime import datetime, timedelta

from lib import logger

##################################################
#                                                #
# Description: Used for JWT Token generation and #
#              Token Verification                #
#                                                #
##################################################

class token:

  #
  # Description: Load in JWT Secret from YAML
  #

  def __init__(self):

    with open(os.path.dirname(__file__) + '/../config/secret.yml', 'r') as db:
      jwt = yaml.load(db)

    setattr(self, 'secret', jwt['secret'])

  #
  # Description: Generate JWT Token for authenticated user
  #

  async def generate_token(self):
    try:
      token = jwt.encode({'exp': datetime.utcnow() + timedelta(hours=3)}, self.secret, algorithm='HS256')
      return token
    except Exception as e:
      log.error('Exception: '+ str(e))
      return False

  #
  # Description: Verifies a supplied token
  #

  async def verify_token(self, payload):
    try:
      for arg in payload.args:
        if not payload.args['token']:
          return False
        else:
          token = payload.args['token'][0]
          if jwt.decode(token, self.secret, algorithms=['HS256']):
            return True
          else:
            return False
    except Exception as e:
      log.error('Exception: '+ str(e))
      return False
