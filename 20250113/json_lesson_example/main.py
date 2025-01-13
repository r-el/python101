import json
from lightBulb import LightBulb

def main():
    with open('data.json', 'r') as file:
        data = json.load(file)
        
    bulb = LightBulb()
    
    # update the object's attributes
    bulb.__dict__.update(data)
    
    print(bulb)

if __name__ == "__main__":
    main()
