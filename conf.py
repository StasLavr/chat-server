import os
from dotenv import load_dotenv
load_dotenv()

db_url = os.environ.get("db_url2")
token = os.environ.get('token')
print(db_url)       