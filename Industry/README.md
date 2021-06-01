# About
```
With a program board, we can do some basic quality of life improvements for setting up industry. 
Also, this LUA could be used to check a group of machines but the included 
status lights on the machines already do a good job of that.

The main point of this script is to aid in starting (or restarting) machines using the same recipe.
```

# Notes
```
You can start a machine via lua without talents. So if you do not have proficiency skills it will start. It will apply the talents, for whom 
ever started the machine so use with caution.
```

# Bugs
```
All machines don't reliably start via lua, but you can start the program 2 or 3 times and it should start all machines. 
Not a bug, but the LUA is using the soft start method to avoid throwing anything away. If you want to reconfigure and the machines are jammed, then fix the jam then restart.
```

# Setup
```
Step 1) Build a normal group of machines like any normal factory. 
Step 2) Load the schematics like any normal factory. 
Step 3) Start the first machine (this is required to get the schematic ID)
Step 4) Link a program board to all machines running the same recipe (machines can be routed to different outputs)
Step 5) Load the LUA, and start the program board. (The easiest way is to just copy the raw to the clipboard)
Step 6) Change the LUA parameters if you'd like. Setting the batch size to zero should start all machines in run 'til full mode.
Step 7) Start the program board a second time (know issue in timing)
Step 8) Verify that the machines are all running.
```

# Simple Schematic Copy (Visual copy)

```lua
This goes into : system.start() 

local batchsize = 500 --export How many to run
local inc_batch = 500 --export Stagger Machine Batch Size.
local always_restart = True --export Use to ignore current machine status.

system.print("Batch Size: "..batchsize.." Stagger Batch "..inc_batch)

-- Copy the First Machine's Schematic
local schematic = slot1.getCurrentSchematic()
if schematic == nil or schematic == 0 then
    system.print("Set First Machine Schematic!")
    return
end

-- Apply the First Machine's Schematic and start the Batches.
local machines = {slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10}
for i,machine in ipairs(machines) do
     if machine == nil then
        system.print("Missing Slot")
     end     
     if machine.getEfficiency() < 0.01 then
        --system.print("Stopping Slot"..i)
        machine.softStop()
     end
     local status = machine.getStatus()
     if status == "STOPPED" or always_restart then
          --system.print("Starting Slot"..i)
		machine.setCurrentSchematic(schematic)
		if batchsize > 0 then
          	machine.startAndMaintain(batchsize + (i-1)*inc_batch)
          else
          	machine.start()
          end

        end
     system.print("Slot"..i.." --- Status: "..machine.getStatus()
        .." --- Eff: "..machine.getEfficiency())
end

unit.exit()
```
