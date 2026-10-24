# Scene File Format Documentation
Like most of the files for both Summon Night DS games, they are both LZ10 compressed.  
This information is for the decompressed file data.  
The game's script files are in `data/scnrts` with the `.rtz` file extension.

## Strings Info
The game's font is Shift-JIS encoded with ASCII support.  
All strings start with a number (one byte) with the string's length in bytes.

## Start of File
### Commands
- The first byte is a list of total commands
- Each command has a "tag" (4-byte integer, little-endian), then a name (string)

### Args
- Also has a list of number of strings.
- I have no clue what these are but some of the strings reference `.h` and `.rts` files.  

### Indexed Commands
- Has total commands
- Pattern is the command "tag" then some "index" (starting from 0 up to the total minus 1)

### Unknown Stuff
- The rest of the file before we see all the strings
- So far there's a number of "total" commands
- Then there is tags referencing commands, then some unknown value
- These unknown values are usually just 1 byte, and with a value of 0x00, but sometimes they are other values and more than 1 byte

## Where the text starts
### Control Codes
There are control codes referenced before the strings but I haven't figured out the entire format.  

#### 0x31
- 9 bytes total (includes control byte)
- One 4-byte integer little-endian
- One 4-byte integer little-endian, sometimes a character value (loads in that character's face graphics?)*

#### 0x65
- 5 bytes total (includes control byte)
- One 4-byte integer little-endian

#### 0x68
- 14 bytes total (includes control byte)
- One 4-byte integer little-endian
- One command tag
- One 4-byte integer little-endian
- One 1-byte value

#### 0x33
- 5 bytes minimum
- One 4-byte integer little-endian
- String

### Notes
A lot of the first/only integers usually seem to be the same value.

### Character Values
In the `main_0002.bin` overlay at `0x2EC80` there is a table of character values with pointers.  
The pointers are relative to the file with an offset of `0x02179740` and point to character names that show up in cutscenes.  
The values are used to figure out which character face graphics to load in, with the value corresponding to `data/evface/ecXXXX.narc` (in base 10).
The values are also sometimes used in the `0x31` text control code.