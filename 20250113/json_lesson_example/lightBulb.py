class LightBulb:
    def __init__(self):
        self.size = -1
        self.type = ""
        self.watt = -1
    
    def __str__(self):
        return f"Size: {self.size}, Type: {self.type}, Watt: {self.watt}"
        
