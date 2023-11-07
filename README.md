# roblox_ssmodules
An old tool used to verify old serversided modules and download them.

Releasing it following the closure of V3rmillion, and the certain death of Roblox exploiting.
See this as an archive for old modules that were used to troll a whole load of people.

### But how does it work?

It checks the `https://assetdelivery.roblox.com/v1/asset/?id=` endpoint, and checks if the module is still available
From there, it downloads it and puts it into a folder, and outputs the used `require()` string into check_success.txt.
Very simple tool, just a fun side-project.
