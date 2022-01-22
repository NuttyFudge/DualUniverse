------------------------------------------------------------------------------
-- FUN
------------------------------------------------------------------------------

function getTime()
    local hoursOffset = -1
    local unixTime = math.floor(system.getTime() + 1506729600) - (60*60*(hoursOffset or 0)) --(Oct. 1, 2017, at 00:00) //1506729600 //1506816000

    local hours = math.floor(unixTime / 3600 % 24)
    local minutes = math.floor(unixTime / 60 % 60)
    local seconds = math.floor(unixTime % 60)

    local unixTime = math.floor(unixTime / 86400) + 719468
    local era = math.floor(unixTime / 146097)
    local doe = math.floor(unixTime - era * 146097)
    local yoe = math.floor((doe - doe / 1460 + doe / 36524 - doe / 146096) / 365)
    --local year = math.floor(yoe + era * 400)
    local doy = doe - math.floor((365 * yoe + yoe / 4 - yoe / 100))
    local mp = math.floor((5 * doy + 2) / 153)
    
    --local year = year + (month <= 2 and 1 or 0)
    local month = math.floor(mp + (mp < 10 and 3 or -9))
    local day = math.ceil(doy - (153 * mp + 2) / 5 + 1)
    
    month = month < 10 and  "0" .. month or month
    day = day < 10 and  "0" .. day or day
    hours = hours < 10 and  "0" .. hours or hours
    minutes = minutes < 10 and  "0" .. minutes or minutes
    seconds = seconds < 10 and  "0" .. seconds or seconds
    
    return (month .. "-" .. day .. " " .. hours .. ":" .. minutes)
end
    
function getKeyTime()
    local hoursOffset = -1
    local unixTime = math.floor(system.getTime() + 1506729600) - (60*60*(hoursOffset or 0)) --(Oct. 1, 2017, at 00:00) //1506729600 //1506816000

    local hours = math.floor(unixTime / 3600 % 24)
    local minutes = math.floor(unixTime / 60 % 60)
    local seconds = math.floor(unixTime % 60)

    local unixTime = math.floor(unixTime / 86400) + 719468
    local era = math.floor(unixTime / 146097)
    local doe = math.floor(unixTime - era * 146097)
    local yoe = math.floor((doe - doe / 1460 + doe / 36524 - doe / 146096) / 365)
    --local year = math.floor(yoe + era * 400)
    local doy = doe - math.floor((365 * yoe + yoe / 4 - yoe / 100))
    local mp = math.floor((5 * doy + 2) / 153)
    
    --local year = year + (month <= 2 and 1 or 0)
    local month = math.floor(mp + (mp < 10 and 3 or -9))
    local day = math.ceil(doy - (153 * mp + 2) / 5 + 1)
    
    month = month < 10 and  "0" .. month or month
    day = day < 10 and  "0" .. day or day
    hours = hours < 10 and  "0" .. hours or hours
    minutes = minutes < 10 and  "0" .. minutes or minutes
    seconds = seconds < 10 and  "0" .. seconds or seconds
    
    return (month .. "_" .. day .. "_" .. hours .. "_" .. minutes)
end
    
function getHour()
    local hoursOffset = -1
    local unixTime = math.floor(system.getTime() + 1506729600) - (60*60*(hoursOffset or 0)) --(Oct. 1, 2017, at 00:00) //1506729600 //1506816000

    local hours = math.floor(unixTime / 3600 % 24)
    local minutes = math.floor(unixTime / 60 % 60)
    local seconds = math.floor(unixTime % 60)

    local unixTime = math.floor(unixTime / 86400) + 719468
    local era = math.floor(unixTime / 146097)
    local doe = math.floor(unixTime - era * 146097)
    local yoe = math.floor((doe - doe / 1460 + doe / 36524 - doe / 146096) / 365)
    --local year = math.floor(yoe + era * 400)
    local doy = doe - math.floor((365 * yoe + yoe / 4 - yoe / 100))
    local mp = math.floor((5 * doy + 2) / 153)
    
    --local year = year + (month <= 2 and 1 or 0)
    local month = math.floor(mp + (mp < 10 and 3 or -9))
    local day = math.ceil(doy - (153 * mp + 2) / 5 + 1)
    
    month = month < 10 and  "0" .. month or month
    day = day < 10 and  "0" .. day or day
    hours = hours < 10 and  "0" .. hours or hours
    minutes = minutes < 10 and  "0" .. minutes or minutes
    seconds = seconds < 10 and  "0" .. seconds or seconds
    
    return day
end
    
function getDay()
    local hoursOffset = -1
    local unixTime = math.floor(system.getTime() + 1506729600) - (60*60*(hoursOffset or 0)) --(Oct. 1, 2017, at 00:00) //1506729600 //1506816000

    local hours = math.floor(unixTime / 3600 % 24)
    local minutes = math.floor(unixTime / 60 % 60)
    local seconds = math.floor(unixTime % 60)

    local unixTime = math.floor(unixTime / 86400) + 719468
    local era = math.floor(unixTime / 146097)
    local doe = math.floor(unixTime - era * 146097)
    local yoe = math.floor((doe - doe / 1460 + doe / 36524 - doe / 146096) / 365)
    --local year = math.floor(yoe + era * 400)
    local doy = doe - math.floor((365 * yoe + yoe / 4 - yoe / 100))
    local mp = math.floor((5 * doy + 2) / 153)
    
    --local year = year + (month <= 2 and 1 or 0)
    local month = math.floor(mp + (mp < 10 and 3 or -9))
    local day = math.ceil(doy - (153 * mp + 2) / 5 + 1)
    
    month = month < 10 and  "0" .. month or month
    day = day < 10 and  "0" .. day or day
    hours = hours < 10 and  "0" .. hours or hours
    minutes = minutes < 10 and  "0" .. minutes or minutes
    seconds = seconds < 10 and  "0" .. seconds or seconds
    
    return day
end

function getMonth()
    local hoursOffset = -1
    local unixTime = math.floor(system.getTime() + 1506729600) - (60*60*(hoursOffset or 0)) --(Oct. 1, 2017, at 00:00) //1506729600 //1506816000

    local hours = math.floor(unixTime / 3600 % 24)
    local minutes = math.floor(unixTime / 60 % 60)
    local seconds = math.floor(unixTime % 60)

    local unixTime = math.floor(unixTime / 86400) + 719468
    local era = math.floor(unixTime / 146097)
    local doe = math.floor(unixTime - era * 146097)
    local yoe = math.floor((doe - doe / 1460 + doe / 36524 - doe / 146096) / 365)
    --local year = math.floor(yoe + era * 400)
    local doy = doe - math.floor((365 * yoe + yoe / 4 - yoe / 100))
    local mp = math.floor((5 * doy + 2) / 153)
    
    --local year = year + (month <= 2 and 1 or 0)
    local month = math.floor(mp + (mp < 10 and 3 or -9))
    local day = math.ceil(doy - (153 * mp + 2) / 5 + 1)
    
    month = month < 10 and  "0" .. month or month
    day = day < 10 and  "0" .. day or day
    hours = hours < 10 and  "0" .. hours or hours
    minutes = minutes < 10 and  "0" .. minutes or minutes
    seconds = seconds < 10 and  "0" .. seconds or seconds
    
    return day
end


------------------------------------------------------------------------------
-- TODO - get the hourly rate + or -
------------------------------------------------------------------------------

-- Look at the last 10, visits for the change
function getHRate(index)
    return 0
end

function saveKL(index, value)
    local index = index
    local kl_value = math.floor(value+0.5) / 1000
   
    local key = index.."_"..getKeyTime()
    databank.setFloatValue(key, json.encode(kl_value))
        
    if not databank.hasKey(key) then
        system.print("failed to save")
    end
    
    system.print("saved "..key.."="..kl_value)
end

function dumpDatabankStatus(index, hub_count)
    local index = index
    local hub_count = hub_count
    
    local keys = databank.getNbKeys()/hub_count
    system.print ("Data Points Saved : "..keys)
    
    local json = json.decode(databank.getKeys())
    for idx,key in ipairs(json) do
        --system.print(key.."="..value)
        if key:match("^"..index.."_") then
            system.print(key.."="..databank.getFloatValue(key))
        end
    end
end

------------------------------------------------------------------------------
-- MAIN
------------------------------------------------------------------------------
--local element_hubs = True --export Use Hub Volume, Else Use Container Volume
local useTheseSettings = True --export override the databank
local hub_volume = 500000 --export Hub Volume or Desired Volume

local text = "Pure Status:" --export Header
local name1 = "Bauxite" --export n1
local name2 = "Coal" --export n2
local name3 = "Hematite" --export n3
local name4 = "Quartz" --export n4
local name5 = "extra5" --export n5
local name6 = "extra6" --export n6
local name7 = "extra7" --export n7
local name8 = "extra8" --export n8
local name9 = "extra9" --export n9
local name10 = "extra10" --export n10

screen.setCenteredText("hello, world!")

--if True == True then
    screen.setCenteredText("saving...")
    --databank.setIntValue("hub_volume", hub_volume)
    databank.setStringValue("text", text)
    databank.setStringValue("name1", name1)
    databank.setStringValue("name2", name2)
    databank.setStringValue("name3", name3)
    databank.setStringValue("name4", name4)
    databank.setStringValue("name5", name5)
    databank.setStringValue("name6", name6)
    databank.setStringValue("name7", name7)
    databank.setStringValue("name8", name8)
    databank.setStringValue("name9", name9)
    databank.setStringValue("name10", name10)
    screen.setCenteredText("saved... uncheck UseTheseSettings")
--    unit.stop()
--else
    screen.setCenteredText("loading...")
    --hub_volume = databank.getIntValue("hub_volume")
    text = databank.getStringValue("text")
    name1 = databank.getStringValue("name1")
    name2 = databank.getStringValue("name2")
    name3 = databank.getStringValue("name3")
    name4 = databank.getStringValue("name4")
    name5 = databank.getStringValue("name5")
    name6 = databank.getStringValue("name6")
    name7 = databank.getStringValue("name7")
    name8 = databank.getStringValue("name8")
    name9 = databank.getStringValue("name9")
    name10 = databank.getStringValue("name10")    
--end

warning_text = "\n\n\n"
text = text.."\n\n"
full = 0
active_hubs = 0
space = " "
    
names = {name1, name2, name3, name4, name5, name6, name7, name8, name9, name10}
hubs = {hub1, hub2, hub3, hub4, hub5, hub6, hub7, hub8, hub9, hub10}
for i=1,10 do
    if hubs[i] == nil then
        goto continue
    end
    volume = hubs[i].getItemsVolume()
    active_hubs = active_hubs + 1
    -- Math for container 
    -- Hubs don't work with getMaxVolume
    full = (100*volume/hub_volume)
    -- Round
    full = math.floor(full+0.5)
    
    -- Status
    text = text.."\n\tHub["..i.." , "..names[i].."]:     "..full.." %"
    if full <= 1 then
        warning_text = warning_text..names[i].." is empty\n"
    elseif full <= 25 then
        warning_text = warning_text..names[i].." is very low\n"
    elseif full <= 50 then
        warning_text = warning_text..names[i].." is low\n"
    end    
    if databank == nil then
        goto continue
    end

    system.print("Volume="..volume)
    saveKL(i, volume)
    ::continue::    
end

-- Update the screen
screen.setCenteredText(getTime().." "..text..warning_text)


-- Update the databank


------------------------------------------------------------------------------
-- DEBUG
------------------------------------------------------------------------------


--system.print("keyTime : "..getKeyTime())
--system.print("debug status:")
dumpDatabankStatus(1,4)
--system.print("done")
--databank.clear()
--dumpDatabankStatus(1,4)

------------------------------------------------------------------------------
-- FIN
------------------------------------------------------------------------------
unit.hide()
unit.exit()
--unit.setTimer()