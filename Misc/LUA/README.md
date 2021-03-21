## Bet Collector

Basic Collector:

Deploy from Blueprint Guide:
- [] Put blueprint + required items in your linked container.
- [] Deploy Construct
- [] Set price on dispencer
- [] Setup RDMS on dispencer... Create a personal/corp RDMS policy if you don't already have one.
- [] Set buy limit on dispencer... 
- [] Set time delay between purchases...
- [] Change Dispencer Tag (Optional)...
- [] Compact When done (need to test).

Build Order - Link the following 
- [] Program Board => Unlock Button
- [] Program Board => Pressure PAd (Clear Status)
- [] Program Board => Screen1,2,3,4
- [] Pressure Pad => Not Gate => Program Board (Restart Program)
- [] Load LUA on to Program Board 
- TODO: LINK LUA HERE
- [] Step on to Pressure Pad to restart.

FAQ/Troubleshooting:
- [] Where to get a blueprint
- [] What if...
- [] Users Manual?

Basic Features: 
- [] LUA Input Params: "Owner", "Value"
- [] LUA Input Names: "Alice", "Bob", "Charles", "Dave".

Planned Features:
- [] Dynamic Number of Players
- [] LUA Input Params: "Prompt", "PAY_OUT_MODE", 
- [] Add DetectionZone for master player ID.
- [] LUA Input Params: "Name1", "Name2", "Name3", "Nam4"
- [] Lua Output - Payout-Mode (First-Only, First/Last, 3-Way)
- [] Lua Output - Slots
- [] Screen Pool/Slots for players 
-   1 - "Player 1" PAID x2
-   2 - "Player 2" PAID x2
-   3 - "Player 3" PAID x1
-   4 - "Open Slot" 
- [] Clear Databank

Subtasks:
- [] Start Bet Button (is it needed?)
- [] Print Status of Players that have paid & Detect when they have paid?
- [] Detect Master Player in detection zone.
- [] Detect Inventory Change
- [] Clear Databank button
- [] Calculate Payout

## Bet Collector, Nice to Haves
- [] Countdown to race start.
- [] Trigger Christmas Tree
- [] Instructions on setting up dispencer (scratch item)
- [] Determine if dispencer can be triggered via pressure pad
- [] Repeat Bet Button (Reload scratch item)

## Industry Machine Monitor
- [] Link to Screen, Databank, Start Button
- [] Check Status of 8 Machines
- [] Load and Save Schematic IDs to Databank

## Vote Machine Variant
- [] Use Dispencer Tag to limit vote
- [] Save Player ID to Databank
