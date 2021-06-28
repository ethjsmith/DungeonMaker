# DungeonMaker
a project I'm experimenting with for generating random "dungeon" maps


# before starting:
what format does this export as ( img? )
can you manually edit the final result? ( that's a stretch goal )
how much input does a user have  ?size? number of rooms? size of each room?
are enemies included? N
how about traps? how specific are traps ?
give room a type, and build based on that like "stone puts down stone tiles, and lays a couple traps of some kind"
basically the idea is "templating "
some way to blend textures would also be really cool

# features to add ::

* [ ] Rooms don't stack on top of each other  
* [ ] rooms move closer to each other when placed, compacting the map, shortening really long hallways


# general idea

* [ ] 0a: does the dungeon have set start / end points:
* [ ] start point, where the generation starts, could be marked as an entrance no specific end point, its a dungeon, not a maze
* [ ] what sort of input comes in on the dungeon level ? size, number of rooms, difficulty ( ratio of traps/objects/whatever )

# how are rooms/ levels represented in the code? and object ?
* [ ] step 0: stuff that happens to a dungeon as a whole
* [ ] step 1: generate room shape
* [ ] step 2: lay down textures on tiles
* [ ] 2a: themes for rooms
* [ ] step 3: resolve texture conflicts
* [ ] step 4: mask/blend textures
* [ ] step 5: place objects/props

# MISC:
how to host this  ( A web app because that's just who I am? )
the process might look like : make a room: choose how many exits, map out the areas that are traversable,
