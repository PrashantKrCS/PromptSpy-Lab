class Telemetry: 

  def __init__(self): 
    self.opens = 0 
    self.clicks = 0 
    self.replies = 0 
    
  def engagement_score(self): 
    return ( 
      self.opens * 0.2 + 
      self.clicks * 0.5 + 
      self.replies * 0.3 
    )
