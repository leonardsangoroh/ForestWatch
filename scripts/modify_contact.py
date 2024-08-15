from dotenv import load_dotenv
load_dotenv()

import os
import sys
from nylas import Client

nylas = Client(
    os.environ.get('NYLAS_API_KEY'),
    os.environ.get('NYLAS_API_URI')
)

grant_id = os.environ.get("NYLAS_GRANT_ID")
contact_id = os.environ.get("CONTACT_ID")

contact = nylas.contacts.update(
  grant_id,
  contact_id,
  request_body={
    'phone_numbers': [{
        "type": "work", "number": "0794807156"
    }]
  }
)

print(contact)   