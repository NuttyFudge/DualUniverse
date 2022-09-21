import json
import time

def printr(recipe):
    print(f"  RID: {recipe['id']} -> {recipe['out'][0]['dn']} ({recipe['out'][0]['id']})")

def printri(recipe):
    # Format List of Inputs
    inputs = ""
    for item in recipe['in']:
        inputs += ", "
        inputs += item['dn']
    inputs = inputs.split(", ")[1:]
    inputs = str(inputs).replace("[","").replace("]", "")

    print(f"  RID: {recipe['id']} -> {recipe['out'][0]['dn']}, Input: {inputs}")

def lookup_machine(collection, item):
    ''' for each machine in the collection, use its helper data, to check if an output matches.'''    
    for i in range(len(collection)):
        helper_data = collection[i].helper
        blacklist = collection[i].blacklist
        for data in helper_data:
            for o in item['out']:
                if blacklist:
                    if o['dn'] in blacklist:
                        o['dn'] = "XXX Blacklisted XXX"
                        continue
                if data in o['dn']:
                    return i
    return None

class Industry():
    def __init__(self, name, helper={}):
        self.name = name
        self.helper = helper
        self.blacklist = None

        self.all_recipes = []
        self.t1_recipes = []
        self.t2_recipes = []
        self.t3_recipes = []
        self.t4_recipes = []      
    
    def add_recipe(self, item):
        if self.blacklist:
            for bl in self.blacklist:
                if bl in item['out'][0]['dn']:
                    raise IndexError

        self.all_recipes.append(item)        
        if item['tier'] == 1 or item['tier'] == 2:
            self.t1_recipes.append(item)
        if item['tier'] == 3:
            self.t2_recipes.append(item)
        if item['tier'] == 4:   
            self.t3_recipes.append(item)
        if item['tier'] == 5: 
            self.t4_recipes.append(item)

### MAIN ####
assembly_meta = {
    "Adjustor", "Ammo", "Assembly", "Atmospheric", "Aileron", "Airlock", "Artist Unknown", "Alarm",
    "Barrier", "Booster", "Brake", "Button", "board", "Bench", "Bonsai", "Bed",
    "Cable", "Cannon", "Canopy", "Carpet", "Container", "Controller", "Core Unit", "Chair", "counter", "controller", "column",
    "Dispenser", "Dispenser", "door", "Door", "Detection", "Databank", "Dresser", "Deployable",
    "Element", "Elevator", "Extractor", "Emitter",
    "Force Field", "Furnace", 
    "gate", "Gate", "Generator", "Gear", "Gyroscope", "Gunner Module",
    "Hover", "hover", "Hologram", "Honeycomb Refinery", "Hatch", "Headlight",
    "Industry", "industry",
    "Market", "Missile", "Mining Unit", "Motherboard",
    "Laser", "Launcher", "Light", "Line",
    "Pressure tile", "Printer", "Plant",
    "operator", "Operator",
    "Node", "Nightstand", 
    "Pipe","Puslar", "Pulsor",
    "Radar", "Rocket", "Recycler", "Railgun", "Resurrection", "Relay", "Receiver", "Refiner", "refinery", "Repair Unit",
    "Space", "Shield Generator", "Sign", "Smelter", "Shower", "Stabilizer", "Shelf", "Switch", "Sofa", "Sink", "scaffolding", "Screen",
    "Table", "Tank", "Territory", "Trash", "Toilet", "Telemeter", "Transponder", 
    "Vertical",
    "Urinal",
    "Warp", "Wing", "Wingtip", "Windshield", "Wooden", "Weapon", "Window", "window", "Wardrobe",
    "Zone",
}
    
collection = []
unknown_recipes = []

collection.append(Industry("Refiner", {"Pure", "Brick product", "Concrete product", "Marble product", "Wood product"}))
collection.append(Industry("Smelter", {"Alloy", "Steel product", "Silumin Product", "Duralumin product", "Calcium Reinforced Copper"}))
collection.append(Industry("3D Printer", {"Fixation", "Casing", "Basic Screen", "Uncommon Screen", "Advanced Screen", "Rare Screen", "Exotic Screen", "Injector", "Carbon Fiber"}))
collection.append(Industry("Metalworks", {"Burner", "Screw", "Basic Pipe", "Uncommon Pipe", "Advanced Pipe", "Frame", "Robotic Arm", "Magnet", "hydraulics", "Electric Engine", "Chamber", "Mechanical Sensor", "Firing System"}))
collection.append(Industry("Electronics", {"Antenna", "Component", "Connector", "Quantum", "Transformer", "Uncommon Light", "Antimatter Core", "Gravity Core", "Core System", "Processor", "Ore Scanner", "Power System", "Control System", "Basic Electronics", "Uncommon Electronics", "Advanced Electronics", "Rare Electronics", "Exotic Electronics"}))
collection[4].blacklist = {"Electronics industry m"}
collection.append(Industry("Glass", {"LED", "Glass product", "Optics", "Laser Chamber", "Warp Cell", "Capsule", "Luminescent", "Optical Sensor", "Antimatter Capsule"}))
collection.append(Industry("Chemical", {"fuel", "Fuel", "plastic product", "Catalyst", "warhead", "Warhead", "Explosive Module", "Biological"}))
collection.append(Industry("Recyler", {"Gas", "Scrap"}))
collection.append(Industry("Honeycomb", {"Aged", "Painted", "Galvanized", "pattern", "Matte", "Polished", "Glossy", "concrete", "brick", "Waxed", "Panel"}))
collection.append(Industry("Assembly Line", assembly_meta))

# Opening JSON file
f = open('recipes_api_dump.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
for item in data:
    # Clean-up
    del item['nanocraftable']
    del item['time']
    #del item['tier']

    # Rename
    v = item.pop('ingredients')
    item['in'] = v
    v = item.pop('products')
    item['out'] = v

    # Rename Ingredients
    ingredients = []
    for i in item['in']:
        # Parse
        id = i.pop('id')
        dn = i.pop('displayNameWithSize')
        qty = i.pop('quantity')
        # Rebuld
        i['id'] = id
        i['dn'] = dn
        i['qty'] = qty
        ingredients.append(i)
    item['in'] = ingredients

    # Rename Products
    products = []
    for p in item['out']:
        # Parse 
        id = p.pop('id')
        dn = p.pop('displayNameWithSize')
        qty = p.pop('quantity')
        # Rebuild
        p['id'] = id
        p['dn'] = dn
        p['qty'] = qty
        products.append(p)
    item['out'] = products

    ### SORT ###
    machine = lookup_machine(collection, item)
    if machine != None:
        try:
            collection[machine].add_recipe(item)
        except IndexError:
            print("Blacklisted Recipe")
            printri(item)
            unknown_recipes.append(item)
    else:
        unknown_recipes.append(item)

# Closing file
f.close()

# Report
for machine in collection:
    print(f"{machine.name} T1: {len(machine.t1_recipes)} T2: {len(machine.t2_recipes)} T3: {len(machine.t3_recipes)} T4: {len(machine.t4_recipes)}")
# :< 
print(f"Unknown {len(unknown_recipes)}")
for item in unknown_recipes:
    printri(item)

#print("Basic")
#for item in collection[4].t1_recipes:
#    printri(item)