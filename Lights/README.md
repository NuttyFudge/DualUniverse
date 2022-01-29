Usage:

<a href="https://github.com/NuttyFudge/DualUniverse/blob/main/Lights/accel.JPG">Accel</a></p>
<a href="https://github.com/NuttyFudge/DualUniverse/blob/main/Lights/brake.JPG">Brake</a></p>

Cirucit Setup: 

Step A) Link the following circuit: 1->2->3
Step B) Then link the program to everything else. 3->4, 3->5, 3->6
Step C) Rename program board (optional)

```
1) pressure-pad
2) or operator
3) program board
4) core
5) screen (optional)
6) long/vertical/square lights 
```

On the program board add fucntion unit.start()
```
-- version 1.0
oldCoords = vec3(core.getConstructWorldPos())
oldTime = system.getTime()
oldSpeed = 0

if screen ~= nil then
  screen.activate()
end

unit.setTimer("brake", 1)
unit.hide()
```

In unit.stop()
```
if screen ~= nil then
    screen.deactivate()
end
```

Finally in the unit.timer("brake")
```
local accel_upper = 20 --export
local accel_lower = -20 --export

function lights(r,g,b)
    -- EDIT ME: Put in slot names for extra lights.
    light = {bl}
    for i=1,10 do 
        if light[i] ~= nil then
        	light[i].setRGBColor(r,g,b)
        	light[i].activate()
        end
    end
    return
end

local speed = vec3(core.getVelocity()):len()
speed = speed*3.6

local newCoords = vec3(core.getConstructWorldPos())

local time = system.getTime()
local elapsedTime = time - oldTime
oldTime = time

local distance = (newCoords - oldCoords):len()

local measuredSpeed = distance*3.6/elapsedTime

oldCoords = newCoords

local accel = speed - oldSpeed
oldSpeed = speed
--accel = math.floor(10*accel)/10

if screen ~= nil then
    local fontsize = 7
    screen.clear()
    
    screen.addText(7,10,fontsize,"Speed: "..math.floor(10*speed)/10)
    screen.addText(7,30,fontsize,"Time: "..elapsedTime)
    screen.addText(7,60,fontsize,"Accel: "..accel)    
end

-- Green/Neutral/Brake

if accel > accel_upper then
    lights(0,200,0)
elseif accel > accel_lower then
    lights(100,100,100)
else
    lights(200,0,0)
end
```
