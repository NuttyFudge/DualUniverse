# DualUniverse

# TODO List

## Schematic Shopping List:
 *) Warp Cell

## Factory:
 *) Virtual Scaffolding
 *) Remote Controller
 *) Laser
 *) Relay, Vertical Light S & XS
 *) Delay Lin
 *) Transfer Units
 *) Warp Cell
 *) Space Engine M
 
## Dispencers:
 * Ore
 * Pures
 * HoneyComb
 * Lights
 * Engines
 * Hovers
 * Airbreak
 * Containers
 * Tanks
 * Scanners S, L 
 * Transfer Unit
 * Adjuster/Stab/Wing
 * Electronics


# RGB Controller 
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
