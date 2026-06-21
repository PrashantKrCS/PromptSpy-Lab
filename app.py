import json 

from flask import Flask 
from flask import render_template 

from simulation import CampaignSimulator 
from telemetry import Telemetry 

app = Flask(__name__) 

telemetry = Telemetry() 
simulator = CampaignSimulator() 

@app.route("/") 
def dashboard(): 
    with open("personas.json") as f: 
        personas = json.load(f) 
    persona = personas[0] 
    
    campaign = simulator.generate_campaign(persona) 
    
    return render_template( 
        "dashboard.html", 
         persona=persona, 
         campaign=campaign, 
         telemetry=telemetry 
     ) 
   
@app.route("/open") 
def open_email(): 
    telemetry.opens += 1 
    return "Email Opened (Simulation)" 
    
@app.route("/click") 
def click_link(): 
    telemetry.clicks += 1 
    return "Link Clicked (Simulation)" 
    
@app.route("/reply") 
def reply(): 
    telemetry.replies += 1 
    return "Reply Recorded (Simulation)" 
    
if __name__ == "__main__": 
    app.run(debug=True)
