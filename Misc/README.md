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
