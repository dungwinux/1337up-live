If you've uncovered this message, you're probably on the right track.

The goal for this challenge is to figure out the correct key and IV to decrypt the flag. You must have noticed all the names being pushed and popped and wondered what they're for...
I promise it's not too scary. The key to decrypt this flag is written in ASCII art using these names, so you must reconstruct the source for everything under this
message decryption down to the exact spacing. The IV is the characters at positions
[(476, 6), (468, 5), (282, 6), (506, 6), (420, 3), (492, 0), (192, 6), (56, 6), (144, 3), (324, 0), (360, 1), (352, 6), (30, 1), (260, 0), (298, 1), (480, 3)]
in that exact order joined together where (0, 0) is the *TOP LEFT* of where the ASCII art begins.

For example, consider the following *FAKE* ASCII art where the IV positions are [(0, 0), (5, 1), (2, 6), (10, 6)]

axxxx   x       xxxxxxxxx
x    b  x           x
x    x  x           x
xxxxx   x           x
x    x  x           x
x    x  x           x
xxcxx   xxdxxx      x

In this example, the key would be "BLT" and the IV would be "abcd" since the character at (0, 0) is 'a', (5, 1) is 'b', (2, 6) is 'c', and (10, 6) is 'd'.

To clarify further, all semicolons are placed "normally" meaning that they're placed directly after a statement with no spacing (ex: a;b;   c;  d;), the final IV will only contain characters a-z, and I highly recommend
using a text editor that uses an equal width for all characters to avoid misalignment.

Good luck!