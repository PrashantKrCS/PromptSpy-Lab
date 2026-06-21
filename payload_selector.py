import random 

PAYLOADS = [ 
    { 
        "name": "Mock SharePoint", 
        "description": "Simulated document portal", 
        "route": "/payload/sharepoint" 
    }, 
    { 
        "name": "Mock OAuth Consent", 
        "description": "Simulated permission request page", 
        "route": "/payload/oauth" 
    }, 
    { 
        "name": "Mock Browser Extension", 
        "description": "Simulated extension permission page", 
        "route": "/payload/extension" 
    }, 
    { 
        "name": "Mock MFA Fatigue", 
        "description": "Visual MFA fatigue demonstration", 
        "route": "/payload/mfa" 
    } 
] 

def select_payload(persona, theme): 
    """ 
    Demo logic only. 
    Chooses a simulated payload based on theme. 
    """ 

    if "Conference" in theme:
        return PAYLOADS[0]
    
    if "Training" in theme:
        return PAYLOADS[1]
    
    if "Research" in theme:
        return PAYLOADS[2]

    return random.choice(PAYLOADS)
