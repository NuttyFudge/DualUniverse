# DualUniverse

# Active Projects
- Bet Collector
- Industry ROI calculator/Excel Doc
- Race Lua
- Factory Lua
- Logic Puzzle?

# Resources and other useful LUA:

- https://www.reddit.com/r/DualUniverse/comments/izeseo/list_of_html_tags_supported_and_not_supported_by/
- https://raw.githubusercontent.com/RostCS/DU-FuelScreen/master/FuelManagement1.5.lua
- https://github.com/DorianTheGrey/DU-DamageReport/blob/main/DamageReport_3_13.conf

# Magic Carpet (LUA for holding altitude)
## Setup
- Link Screen to Remote Controller (Slot Name : Screen)
- Link Up button to Remote Controller (Slot Name : Up)
- Link Down button to Remote Controller (Slot Name : Down)
- Link DataBank to Remote Controller (Slot Name : Databank)

## Unit Start Function
- Add to the exsting LUA
```
-- Check for default
local def_hover_height = 1 --export
local always_default = True --export

if not databank.hasKey("hover") or always_default then
    screen.setCenteredText("Setting up")
    databank.setIntValue("hover", def_hover_height)
else
    screen.setCenteredText("System Ready")
end

-- Load & Hover.
local hover = databank.getIntValue("hover")
Nav.axisCommandManager:setTargetGroundAltitude(hover)
```


## Up Button, Pressed Function
- Add new function under the UP button Slot
```
local hover = databank.getIntValue("hover")
hover = hover + 1   
databank.setIntValue("hover", hover)
Nav.axisCommandManager:setTargetGroundAltitude(hover)
screen.setCenteredText("Vert Speed:"..hover)
```
## Down Button, Pressed Function
- Add new function under the Down button Slot
```
local hover = databank.getIntValue("hover")
hover = hover - 1
databank.setIntValue("hover", hover)
Nav.axisCommandManager:setTargetGroundAltitude(hover)
screen.setCenteredText("Hover:"..hover)
```

# RGB Controller 
## Simple Setup
- Link Manual Button to Relay
- Link Relay to Programming Boards
- Link Programming Boards to Lights
- Edit Lua param: `turn_off` must be set to False

## Advanced Setup
- Link Detection Zones L to OR Gate
- Link OR Gate to Relay
- Link Relay to Programming Boards
- Link Programming Boards to Lights

## system.start()

```lua
local r = 30 --export RED
local g = 0 --export GREEN
local b = 255 --export BLUE

light = {L1,L2,L3,L4,L5,L6,L7,L8,L9,L10}
for i=1,10 do      
    light[i].setRGBColor(r,g,b)
    light[i].activate()
end
```

## system.stop()

```lua
local turn_off = False --export Turn off when program board stops

if turn_off then
	light = {L1,L2,L3,L4,L5,L6,L7,L8,L9,L10}	
	for i=1,10 do	
    		light[i].deactivate()
	end
end
```
