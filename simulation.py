import random

from templates import PRETEXTS
from templates import EMAIL_TEMPLATE
from payload_selector import select_payload

class CampaignSimulator:

    def generate_campaign(self, persona):

        theme = random.choice(PRETEXTS)

        email = EMAIL_TEMPLATE.format(
            theme=theme, name=persona["name"], interest=persona["interest"]
        )

        payload = select_payload(persona, theme)

        return {"theme": theme, "email": email, "payload": payload}
