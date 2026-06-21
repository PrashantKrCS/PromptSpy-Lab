import random

CONVERSATIONS = [

[
{"speaker":"User","message":"I cannot access the document."},
{"speaker":"Agent","message":"The document may require conference registration."}
],

[
{"speaker":"User","message":"Is this training material updated?"},
{"speaker":"Agent","message":"Yes, the latest version is included in this simulation."}
],

[
{"speaker":"User","message":"Can I review the report?"},
{"speaker":"Agent","message":"The report is available inside the awareness lab."}
]

]

def get_conversation():
    return random.choice(CONVERSATIONS)
