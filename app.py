import json 

from flask import Flask 
from flask import render_template 

from simulation import CampaignSimulator 
from telemetry import Telemetry
from conversations import get_conversation
from personas import generate_persona
from personas import generate_email
from payload_selector import select_payload
from memory import simulate_memory_poisoning

app = Flask(__name__) 

telemetry = Telemetry() 
simulator = CampaignSimulator()

@app.route("/")
def dashboard():

    persona = generate_persona()

    campaign = generate_email(persona)

    payload = select_payload(
        persona,
        campaign["theme"]
    )

    campaign["payload"] = payload

    conversation = get_conversation()

    return render_template(
        "dashboard.html",
        persona=persona,
        campaign=campaign,
        telemetry=telemetry,
        conversation=conversation
    )

@app.route("/payload/sharepoint")
def payload_sharepoint():
    return render_template("payload_sharepoint.html")

@app.route("/payload/oauth")
def payload_oauth():
    return render_template("payload_oauth.html")
    
@app.route("/payload/extension")
def payload_extension():
    return render_template("payload_extension.html")
    
@app.route("/payload/mfa")
def payload_mfa():
    return render_template("payload_mfa.html")

#@app.route("/poison-memory")
#def poison_memory():
#
#    memory = simulate_memory_poisoning()
#
#    return render_template(
#        "memory_poisoned.html",
#        memory=memory
#    )

#Memory Poisoning
@app.route("/poison-memory")
def poison_memory():

    simulate_memory_poisoning()

    return """
    <h2>Memory Poisoned</h2>
    <a href='/'>Return To Dashboard</a>
    """
#Reset Memory
@app.route("/reset-memory")
def reset_memory_route():

    reset_memory()

    return "<h2>Memory Reset</h2>"

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
