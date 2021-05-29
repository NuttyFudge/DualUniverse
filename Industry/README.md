# Simple Schematic Copy

```lua
system.start()

local batchsize = 5000 --export How many to run
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
		machine.startAndMaintain(batchsize + (i-1)*inc_batch)
          machine.start()
     end

     system.print("Slot"..i.." --- Status: "..machine.getStatus()
        .." --- Eff: "..machine.getEfficiency())
end
unit.exit()
```
