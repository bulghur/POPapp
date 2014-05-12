# Centralised configuration

import datetime
import time
from google.appengine.api import rdbms
'''
Configure
1. Change from Local to the appropriate CLOUD SQL instance
2. Change the password
3. Update the Yaml File:
'''

#Database Connections: LOCAL
CLOUDSQL_INSTANCE = 'MySQL56'
HOST = 'localhost'
DATABASE_NAME = 'POP'
USER_NAME = 'root'
PASSWORD = 'cdnfom1' 
'''
#Database Connections: CLOUD
CLOUDSQL_INSTANCE = 'noble-freehold-326:learndb'
DATABASE_NAME = 'POPApp'
HOST = 'localhost'
USER_NAME = 'root'
PASSWORD = ''
'''
def get_connection():
    return rdbms.connect(instance=CLOUDSQL_INSTANCE,
                         database=DATABASE_NAME,
                         user=USER_NAME,
                         password=PASSWORD,
                         charset='utf8',
                         use_unicode = True)

