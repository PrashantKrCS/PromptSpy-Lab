import random 

from templates import PRETEXTS 
from templates import EMAIL_TEMPLATE 

class CampaignSimulator: 
    def generate_campaign(self, persona): 
        
        theme = random.choice(PRETEXTS) 
        
        email = EMAIL_TEMPLATE.format( 
            theme=theme, 
            name=persona["name"], 
            interest=persona["interest"] 
         ) 
         
         return { 
            "theme": theme, 
            "email": email 
         }
