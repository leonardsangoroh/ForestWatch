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

contact = nylas.contacts.create(
  grant_id,
  request_body={
    "middleName": "AA-ForestWatch",
    "surname": "AA-ForestWatch",
    "notes": "Tell me anything about forests!",
    "emails": [{"type": "home", "email": "leonardsangoroh@gmail.com"}],
    "phoneNumbers": [{"type": "work", "number": "0794807156"}],
    "webPages": [{"type": "work", "url": "https://www.linkedin.com/in/leonard-sangoroh-3113461b6/"}]
  }
)

print(contact)  