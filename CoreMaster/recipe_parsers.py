import json
import time

def printr(recipe):
    print(f"  RID: {recipe['id']} -> {recipe['out'][0]['dn']} ({recipe['out'][0]['id']})")

def printri(recipe, max_inputs=3):
    # Format List of Inputs
    inputs = ""
    for item in recipe['in'][:3]:
        inputs += ", "
        inputs += item['dn']
    inputs = inputs.split(", ")[1:]
    inputs = str(inputs).replace("[","").replace("]", "")

    print(f"  RID: {recipe['id']} = {recipe['out'][0]['dn']} << {inputs}")

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

class CLI():

    def __init__(self, data, debug=False): 
        # Cache of everything
        self.collection = []
        self.unknown_recipes = []
        self.machines = []
        recipes = [] 
        self.ore_costs = {
            "Pure Oxygen" : 0,
            "Pure Hydrogen" : 0,
            "Catalyst 3" : 0,
            "Catalyst 4" : 0,
            "Catalyst 5" : 0,
            "Bauxite"  : 25,
            "Coal"     : 25,
            "Hematite" : 25, 
            "Quartz"   : 25,             
            "Chromite" : 40,
            "Natron"   : 40,
            "Limestone" : 30,
            "Malachite" : 30,
            "Acanthite" : 70,
            "Garnierite" : 60,
            "Petalite"   : 120,
            "Pyrite"     : 50,
            "Cobaltite"  : 250,
            "Cryolite"   : 250,
            "Kolbeckite" : 250,
            "Gold nuggets" : 250,
            "Columbite"  : 500,
            "Ilmenite"   : 500,
            "Vanadinite" : 500,
            "Rhodonite"  : 500,
        }
        metalwork_meta = [
            "Basic Pipe", "Uncommon Pipe", "Advanced Pipe",
            "Burner",
            "Chamber",
            "Electric Engine",
            "Firing System",
            "hydraulics",
            "Frame",
            "Magnet", 
            "Mechanical Sensor", 
            "Screw",  
            "Robotic Arm",
            "Singularity"
        ]
        assembly_xs = [
            "Adjustor XS", "Adjustor S", "Atmospheric Airbrake s",
            "Airbrake S", "artist", "button", "Barrier S", "Barrier M", "Barrier corner",
            "Container Hub xs",
            "program board xs", "Bench", "Carpet", "Remote Controller", "chair surface", "encampment chair", "wooden chair",
            "wooden armchair", "counter xs", "steel column", "Detection Zone", "Decorative",
            "Databank", "Dresser M", "Deployable", "Elevator", "Extractor xs", "Emitter xs",
            "Force Field", "Gyroscope",
            "Keyboard Unit",
            "Light Detector xs",
            "Hologram", "Hatch", "Headlight xs", "Launcher", "Line XS",
            "Pressure tile xs", "Plant",
            "operator xs", "Operator xs",
            "Retro-rocket Brake M",
            "Nightstand", "Wooden armchair s",
            "Pipe", "Relay", 
            "Sign", "Shower", "Shelf", "Switch", "Sink", 
            "Wooden low table M", "Trash", "Toilet", "Telemeter", "Transponder", "Screen", "Teleportation Node",
            "Urinal", "Virtual scaffolding projector xs",
            "Wardrobe", "Wingtip M", "Wingtip S",
            "Zone",
        ]
        assembly_s = [
            "Adjustor M",
            "Airbrake m",
            "Chair S",
            "dresser",   
            "Plant",
            "Resurrection Node S",     
            "Retro-rocket Brake M",
            "Rocket Fuel Tank XS",
            "Wooden table l", "Wooden table m",
            "Resurrection",
            "Surrogate Pod Station m", "Surrogate VR Station m",
            "Wingtip L", "Wooden wardrobe m", "Market Pod s",
            "Wooden Sofa S", "Wooden dresser M", "Wooden table m", "Wooden table l", "Window", "window"
        ]
        assembly_m = [
            "Adjustor l",
            "Airbrake l",
            "industry", "Industry"
            "Wing m",
            "Wing variant m",
            "Retro-rocket Brake l",
            "Rocket Fuel Tank l"
        ]
        assembly_l = [
            "Warp Drive l",
            "Rocket Fuel Tank L"
        ]
        assembly_xl = [
            "Deprecated material refinery",
            "Deprecated Honeycomb refinery",
            "Territory Unit",
            "Deep Space Asteroid Tracker xl",
            "Warp Beacon xl",
        ]
        assembly_meta = [
            "Adjustor", "Ammo", "Assembly", "Atmospheric", "Aileron", "Airlock", "Artist Unknown", "Alarm",
            "Barrier", "Booster", "Brake", "Button", "board", "Bench", "Bonsai", "Bed",
            "Cable", "Cannon", "Canopy", "Carpet", "Container", "Controller", "Core Unit", "Chair", "counter", "controller", "column", "Core",
            "Dispenser", "Dispenser", "door", "Door", "Detection", "Databank", "Dresser", "Deployable",
            "Element", "Elevator", "Extractor", "Emitter", "Engine", "engine",
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
            "Warp", "Wing", "Wingtip", "Windshield", "Windshield corner", "Windshield flat", "Windshield triangle", "Windshield tilted", "Wooden", "Weapon", "Window", "window", "Wardrobe",
            "Zone"
        ]

        # Update Each Size of Assembly Line
        for item in assembly_meta:
            assembly_xs.append(f"{item} xs")
            assembly_s.append(f"{item} s")
            assembly_m.append(f"{item} m")
            assembly_l.append(f"{item} l")
            assembly_xl.append(f"{item} xl")

            assembly_xs.append(f"{item} XS")
            assembly_s.append(f"{item} S")
            assembly_m.append(f"{item} M")
            assembly_l.append(f"{item} L")
            assembly_xl.append(f"{item} XL")

        # print(assembly_xs)

        self.collection.append(Industry("Refiner", {"Pure", "Brick product", "Concrete product", "Marble product", "Wood product"}))
        self.collection.append(Industry("Smelter", {"Alloy", "Stainless Steel product", "Steel product", "Silumin Product", "Duralumin product", "Calcium Reinforced Copper"}))
        self.collection.append(Industry("3D Printer", {"Fixation", "Casing", "Basic Screen", "Uncommon Screen", "Advanced Screen", "Rare Screen", "Exotic Screen", "Injector", "Carbon Fiber"}))
        self.collection.append(Industry("Metalworks", metalwork_meta))
        self.collection.append(Industry("Electronics", {"Antenna", "Component", "Connector", "Quantum", "Transformer", "Uncommon Light", "Antimatter Core", "Gravity Core", "Core System", "Processor", "Ore Scanner", "Power System", "Control System", "Basic Electronics", "Uncommon Electronics", "Advanced Electronics", "Rare Electronics", "Exotic Electronics"}))
        #self.collection[4].blacklist = {"Electronics industry m"}
        self.collection.append(Industry("Glass", {"LED", "Glass product", "Optics", "Laser Chamber", "Warp Cell", "Capsule", "Luminescent", "Optical Sensor", "Antimatter Capsule"}))
        self.collection.append(Industry("Chemical", {"fuel", "Fuel", "plastic product", "Catalyst", "warhead", "Warhead", "Explosive Module", "Biological"}))
        self.collection.append(Industry("Recyler", {"Gas", "Scrap"}))
        self.collection.append(Industry("Honeycomb", {"Aged", "Painted", "Galvanized", "pattern", "Matte", "Polished", "Glossy", "concrete", "brick", "Waxed", "Panel"}))
        self.collection.append(Industry("Assembly Line xs", assembly_xs))
        self.collection.append(Industry("Assembly Line S", assembly_s))
        self.collection.append(Industry("Assembly Line M", assembly_m))
        self.collection.append(Industry("Assembly Line L", assembly_l))
        self.collection.append(Industry("Assembly Line XL", assembly_xl))
        # self.collection.append(Industry("Assembly Line", assembly_meta))

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
            machine = self.lookup_machine(item)
            if machine != None:
                try:
                    self.collection[machine].add_recipe(item)
                except IndexError:
                    print("Blacklisted Recipe")
                    printri(item)
                    self.unknown_recipes.append(item)
            else:
                self.unknown_recipes.append(item)

        # Closing file
        f.close()

        # Report
        print("Loaded :")
        for machine in self.collection:
            print("{:>25}".format(machine.name), end="")
            print(f" T1: {len(machine.t1_recipes)} T2: {len(machine.t2_recipes)} T3: {len(machine.t3_recipes)} T4: {len(machine.t4_recipes)}")
        print("")

        if debug:
            pass
            #print(f"Unknown {len(self.unknown_recipes)}")
            #for item in self.unknown_recipes:
            #    printri(item)

            #machine = self.collection[1]
            #for item in machine.t1_recipes:
            #    printri(item)

    def lookup_machine(self, item):
        for i in range(len(self.collection)):
            helper_data = self.collection[i].helper
            blacklist = self.collection[i].blacklist
            for data in helper_data:
                for o in item['out']:
                    if blacklist:
                        if o['dn'] in blacklist:
                            o['dn'] = "XXX Blacklisted XXX"
                            continue
                    if data in o['dn']:
                        return i
        return None

    def find_recipe(self, recipe):
        ret = []
        reps = []
        for machine in self.collection:
            rrs = [machine.t1_recipes, machine.t2_recipes, machine.t3_recipes, machine.t4_recipes]
            for s in rrs:
                #if machine in ret:
                #    break
                for r in s:
                    #if machine in ret:
                    #    break
                    if recipe in r['out'][0]['dn']:
                        #if machine in ret:
                        #    break
                        ret.append(machine)
                        reps.append(r)
        return ret, reps

    def find_recipe_inputs(self, recipe):
        return_recipes = []
        return_machines = []
        for machine in self.collection:
            #recipe_set = self.collection = [machine.t1_recipes, machine.t2_recipes, machine.t3_recipes, machine.t4_recipes]
            for recipe_set in machine.all_recipes: ### recipe_self.collection:
                for r in recipe_set:
                    # For 
                    if recipe in r['out'][0]['dn']:
                        return_machines.append(machine)
                        return_recipes.append(r)
        return return_recipes, return_machines

    def unit_price_search(self, recipe, depth=5):
        cost = self.ore_costs.get(recipe['dn'], 0)
        if cost == 0:
            lookup_recipe = self.find_recipe(recipe)
            cost += self.find_cost(lookup_recipe, depth-1)
        return cost

    def find_cost(self, recipe, batch_cost=False, depth=5):
        if depth < 0:
            return 0

        dn = recipe['out'][0]['dn']
        print(f"\n{dn} cost:")

        cost = 0
        qty_out = int(recipe['out'][0]['qty'])

        # Deal with biproduct
        try:
            if recipe['out'][1]:
                pass
        except:
            pass

        for item in recipe['in']:
            unit_price = self.unit_price_search(item)
            cost += unit_price * item['qty']
            print(f" + {item['dn']} @ ", end="")
            print("{:.2f}".format(unit_price))
        
        print("Batch Cost :: ${:.2f}".format(cost), end="")
        print(" Per Unit :: ${:.2f}\n".format(cost/qty_out))
        if cost > 0 and dn not in self.ore_costs:
            self.ore_costs[dn] = cost/qty_out
        
        # Batch Size
        if batch_cost:
            return cost
        return cost / qty_out

    def run(self):
        CLI = True
        while(CLI):
            mode = input("D to dump Names, E to Exit, S for Search, W for Where Used, C to Clear, P for Price :: ")
            if mode == "E":
                CLI = False

            if mode == "D":
                names = {}
                #for machine in selected_machines:
                #    for recipes in machine.all_recipes:
                for recipe in selected_recipes:
                        for item in recipe["in"]:
                            names[item["id"]] = item["dn"]

                        for item in recipe["out"]:
                            names[item["id"]] = item["dn"]
                            
                    #print(self.names) 
                for item in names:
                    print(f"r[{item}] = \"{names[item]}\"")

            if mode == "C":
                selected_machines = []
                selected_recipes = [] 

            if mode == "S":
                search = input("Search for Machine > Recipe :: ")
                selected_machines, selected_recipes = self.find_recipe(search)
                if selected_machines:
                    for name, out in zip(selected_machines, selected_recipes):
                        print(f"{name.name} > {out['out'][0]['dn']} <", end="")
                        for item in out['in']:
                            print(f" {item['dn']} ", end="")
                        print("")        
                else:
                    print("Unfound")

            if mode == "W":
                search = input("Search for Where-Used :: ")
                selected_machines, selected_recipes = self.find_recipe_inputs(search)
                if selected_machines:
                    for name, out in zip(selected_machines, selected_recipes):
                        print(f"{name.name} > {out['out'][0]['dn']} <", end="")
                        for item in out['in']:
                            print(f" {item['dn']} ", end="")
                        print("")        
                else:
                    print("Unfound")

            if mode == "P":
                for r in selected_recipes:
                    try:
                        self.find_cost(r)
                    except RecursionError:
                        time.sleep(3)
                        print(f"Recursion Error: {r}")

# MAIN
# Opening JSON file
f = open('recipes_api_dump.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)

# Fixup
data.append({
    "id":2984358477,
    "tier":2,
    "time":750,
    "nanocraftable":False,
    "ingredients":
        [
        {"quantity":75,"id":2147954574,"displayNameWithSize":"Pure Chromium"},
        {"quantity":100,"id":198782496,"displayNameWithSize":"Pure Iron"},
        {"quantity":50,"id":159858782,"displayNameWithSize":"Pure Carbon"}
    ],
    "products":
        [
        {"quantity":75,"id":2984358477,"displayNameWithSize":"Stainless Steel product"}
    ]
})

# Main Loop
cli = CLI(data)
cli.run()