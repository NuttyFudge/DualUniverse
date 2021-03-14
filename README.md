# DualUniverse

# Resources

https://www.reddit.com/r/DualUniverse/comments/izeseo/list_of_html_tags_supported_and_not_supported_by/



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
