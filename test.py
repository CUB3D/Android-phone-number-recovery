import sqlite3
from pprint import pprint

db = sqlite3.connect("./contacts2.db")

a = db.execute("select _id,display_name from raw_contacts")

data = []
for contact in a.fetchall():
    data.append({"Id": contact[0], "Name": contact[1]})

for contact in data:
    a = db.execute("select normalized_number from phone_lookup where raw_contact_id=" + str(contact["Id"]))
    contact["Numbers"] = a.fetchall()

for contact in data:
    print(contact["Name"] + ", " + " ".join([x[0] for x in contact["Numbers"]]))
