
## .blend utilities

This repository contains two scripts: 
* `list_file_blocks.py` shows a complete list of "file blocks" in a .blend file and information from its header, including positions in the file.
* `repair.py` is a very minimal script for combining two binary files

## Why
The reason I wrote this was originally because of the `Loading 'C:\example.blend' failed: Failed to read blend file 'C:\example.blend': Missing DNA block` error message while trying to load a damaged blender file. In my case, the data I needed were not actually in the file, but it *could* in theory help with this error if you have a file that contains the right data.

## Usage
**Always create a copy of each file first.**

`list_file_blocks.py` just takes one argument - path to the .blend file. It will output a list of blender's "file blocks". Using this you can for example locate the last complete block in the damaged file. Knowing the block code and position of the last block, it is possible to then locate it in a hex editor. Then knowing the size of the block, you know if it is not complete.

Example: `python list_file_blocks.py test.blend`

`repair.py` takes 4 arguments. First two are the damaged file and a known good file (empty or copy of a last working save), in that order. Third argument is a position in the damaged file of the end of the last complete file block. The script will take the contents of the file up to this point and output it to a new file. Fourth argument is a starting position in the second file from which to take data and append to the newly created file. Probably easiest is to just put 12 here (the length of the header). That way there will be duplicated data in the file, but blender usually repairs bad data well and you can then just delete what is not needed from withing blender when you have a file that can be opened.

This creates a new file with the same name as the original damaged file and a .repaired extension in the current folder.

Example: `python repair.py damaged.blend good.blend 89047496 12`

## Links
More info about the .blend file structure at [http://www.atmind.nl/blender/mystery_ot_blend.html](http://www.atmind.nl/blender/mystery_ot_blend.html)