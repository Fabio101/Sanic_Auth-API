#
# Imports
#

import os
import yaml
import pymysql.cursors
from lib import logger
from sanic.exceptions import ServerError

##################################################
#                                                #
# Description: Main Database class used for all  #
#              DB Interaction                    #
#                                                #
##################################################

class database:

  #
  # Description: Load in DB Creds from ENV or YAML and set Class attributes for easy access  
  #

  def __init__(self):

    with open(os.path.dirname(__file__) + '/../config/database.yml', 'r') as db:
      config = yaml.load(db)

    db = os.getenv('db_name', config['db_name'])
    host = os.getenv('db_host', config['db_host'])
    user = os.getenv('db_user', config['db_user'])
    password = os.getenv('db_pass', config['db_pass'])

    setattr(self, 'db', db)
    setattr(self, 'host', host)
    setattr(self, 'user', user)
    setattr(self, 'password', password)

  #
  # Description: Executes a query to the database and returns the result data
  #

  async def query(self, query, *args, commit=False, select=False):

    try: 
       setattr(self, 'conn', pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db, cursorclass=pymysql.cursors.DictCursor))
    except Exception as e:
       logger.log.error('Exception: '+ str(e))
       return False

    try:
      cursor = self.conn.cursor()
      cursor.execute(query, list(args))

      if commit == True:
        try:
          self.conn.commit()
        except Exeption as e:
          logger.log.error('Exception: '+ str(e))
          return False

      if select == True:
        sql_results = cursor.fetchall()
        if cursor.rowcount > 0:
          return sql_results
        else:
          return False
      return True

    except Exception as e:
      logger.log.error('Exception: '+ str(e))
      return False

    finally:
      self.conn.close()