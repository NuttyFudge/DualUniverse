``` lua

local r = 128 --export RED
local g = 0 --export GREEN
local b = 255 --export BLUE

function test(r,g,b)
    -- Known Bugs, your welcome NQ.
    if r > 255 or r < 0 then
        r = 0
    end
    if g > 255 or g < 0 then
        g = 0
    end
    if b > 255 or b < 0 then
        b = 0
    end
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

unit.setTimer("n", 1)

```
