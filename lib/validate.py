#
# Imports
#

from validate_email import validate_email
from lib import database

##################################################
#                                                #
# Description: Used for all data validation      #
#                                                #
##################################################

db = database.database()

class validate:

  #
  # Description: Queries the database to determine the existence of a user email
  #

  async def check_user(self, email):

    result = await db.query("SELECT * FROM users WHERE email = %s", email, select = True)

    if result:
      return True
    else:
      return False

  #
  # Description: Validates a JSON Payload
  #

  async def check_payload(self, payload, *args):

    if payload.json:
      data = payload.json

      if len(args) > 0:
        for arg in args:
          try:
            if not data[arg]:
              return False
          except Exception as e:
            return False
      return True
    else:
      return False

  #
  # Description: Validates user email syntax and DNS
  #

  async def check_email(self, email):
  	#Leaving DNS validation off for nowt
    if validate_email(email, verify=False) == True:
      return True
    else:
      return False