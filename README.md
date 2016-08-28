# rgb2colorname
Provide the name of a color closest to an RGB value provided.
Input: ["RGB","221","185","135"]
Output: ["burlywood","222","184","135","gray"]

We recognize that certain names have different associations in different parts of the world.

Alternative RGB hex and HCL representations are processed by another API.

Text in the heading line begin with an underline so it sorts to the top.

Column "_Hex" is the Hexadecimal combination of 3 RGB() numbers.
The column contains a leading dash because of the bad way Microsoft Excel handles hex numbers.
The single quote makes Excel see the six-characters as text rather than numbers.
The conversion to hex was done using this Excel formula:

   =concatenate("'",DEC2HEX(B678,2),DEC2HEX(C678,2),DEC2HEX(D678,2))

Column "_Title" contains color names that in "Title" case,
with a capitalize first letters of every word.
SVG has names in all lower case.

Column "_Name" are dashes between compound words for X11.

Column "_X11" is needed because color names are from a combination of sources,
which compete for the same color name and number.

   * "X11" is from https://en.wikipedia.org/wiki/X11_color_names
   X11 color names first defined in 1985.

   * https://cgit.freedesktop.org/xorg/app/rgb/tree/rgb.txt

Column "_Gray" contains either "gray" or "grey" to differentiate then alternate spellings.
This doubles the number of colors defined as gray/grey.

Column "_SVG" is used to designate names in SVG. Color numbers differs between SVG and X11 for 
"gray", "gray", "green", "maroon" and "purple".
These exceptions have "diff" in X11 lines.
SVG has "darkgray" while X11 does not.

   * "SVG" is from https://www.w3.org/TR/SVG/types.html#ColorKeywords

Additional columns may be added because there are other color names, such as:

   * Pantone (proprietary).

   * https://en.wikipedia.org/wiki/Crayola#Colors

