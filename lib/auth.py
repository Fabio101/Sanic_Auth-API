#
# Imports
#

from bcrypt import hashpw, gensalt

from lib import database
from lib import validate
from lib import token

##################################################
#                                                #
# Description: Used for User authentication and  #
#              returns JWT Token                 #
#                                                #
##################################################

db = database.database()
val = validate.validate()
jwt = token.token()

class authenticate:

  #
  # Description: Checks a user and grants a token if valid
  #

  async def auth(self, payload):

    check_payload = await val.check_payload(payload, 'email', 'password')
    if check_payload:
      check_email = await val.check_email(payload.json['email'])
      check_user = await val.check_user(payload.json['email'])
      result = await db.query("SELECT password FROM users WHERE email = %s", payload.json['email'], select = True)
      if result:
        compare_password = hashpw(payload.json['password'].encode('utf-8'), result[0]['password'].encode('utf-8')) == result[0]['password'].encode('utf-8')
      else:
        compare_password = False
    else:
      check_email = False
      check_user = False

    token = await jwt.generate_token()

    if check_payload:
      if check_email:
        if check_user:
          if result:
            if compare_password:
              if token:
                return {"token": token}, 200
              else:
                return {"error": "Failed to generate token! Check Server Logs"}, 500
            else:
              return {"error": "Invalid Password"}, 400
          else:
            return {"error": "Failed to execute query! Check Server Logs"}, 500
        else:
          return {"error": "Email does not exist!"}, 400
      else:
        return {"error": "Email is not valid!"}, 400
    else:
      return {"error": "Bad Payload!"}, 400