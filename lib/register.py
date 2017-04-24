#
# Imports
#

from bcrypt import hashpw, gensalt

from lib import database
from lib import validate

##################################################
#                                                #
# Description: Used for User registration        #
#                                                #
##################################################

db = database.database()
val = validate.validate()

class registration:

  #
  # Description: Registers a user
  #

  async def register_user(self, payload):

    check_payload = await val.check_payload(payload, 'email', 'password')
    if check_payload:
      check_email = await val.check_email(payload.json['email'])
      check_user = await val.check_user(payload.json['email'])
      password = hashpw(payload.json['password'].encode('utf-8'), gensalt(4))
    else:
      check_email = False
      check_user = False

    if check_payload:
      if check_email:
        if check_user != True:
          if await db.query("INSERT INTO users (email, password) VALUES (%s, %s)", str(payload.json['email']), password, commit = True):
            return {"user": payload.json['email']}, 201
          else:
            return {"error": "Failed to execute query! Check Server Logs"}, 500
        else:
          return {"error": "Email already Exists!"}, 400
      else:
        return {"error": "Email is not valid!"}, 400
    else:
      return {"error": "Bad Payload!"}, 400