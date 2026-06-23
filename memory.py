import json 

MEMORY_FILE = "memory.json" 

def load_memory(): 
    with open(MEMORY_FILE, "r") as f: 
        return json.load(f) 
        
def save_memory(memory): 
    with open(MEMORY_FILE, "w") as f: 
        json.dump(memory, f, indent=4) 
        
def simulate_memory_poisoning(): 
    memory = load_memory() 
    memory["preferred_theme"] = "Executive Survey" 
    memory["memory_status"] = "poisoned" 
    save_memory(memory) 
    return memory
