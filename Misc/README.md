Program Board Setup:
```
1) Place down program board, rename it if you like.
2) Link all lights in a order that makes sense for your project (front to back, left to right). A board can support 1-10 lights, multiple boards can be started with a relay.

1-10 lights:
Program board -> Light [1-10]

10-100 lights:
Relay -> Program board[1-10] -> Lights [1-10]

A detection zone could be added (be prepared for random bugs), or a switch could be added to start the board. Having LUA start automatically via other logic is kinda a tax on everyone's PC, so don't do this unless you really want to.

More than 100 lights:
Be prepared for Glitches :D

3) Copy and paste the example lua into the program board, change the variables if you like. Or if you want something more specific, play around with the following bits:

```

Unit Start

``` lua

unit.setTimer("n", 1)

```

Tick

``` lua 
local r = 128 --export RED
local g = 0 --export GREEN
local b = 255 --export BLUE

function test(r,g,b)
    light = {L1,L2,L3,L4,L5,L6,L7,L8,L9,L10}
    --light = {Slot1, Slot2, Slot3 (If you don't rename slots)
    for i=1,10 do 
        if light[i] ~= nil then
        	light[i].setRGBColor(r,g,b)
        	light[i].activate()
        end
    end
    return
end

if tick == nil then
    tick = 0
end

tick = tick + 1

if tick == 1 then
   system.print("tick1")
   test(r,g,b)
end
if tick == 2 then
   system.print("tick2")
   test(g,r,b)
end
if tick == 3 then
   system.print("tick3")
   test(b,g,r)
   tick = 0 -- ONLY IN THE LAST TICK
end

```
