The program <strong>rb2colorname.py</strong>
invokes and algorithm that identifies the name of a color closest to an RGB value provided.

* Input: ["221","185","135"] are RGB (Red Green Blue) values between 0 - 256.

   Alternative RGB hex and HCL representations are processed by another API.

* Output: ["burlywood","222","184","135","gray"]



## Usage #

Certain names have different associations in different parts of the world.
So this may not see much use.
But this is a fun exercise to make use of the Python numpy library's closest-neighbor functions.


## Processing #

0. The 3-dimensional array in the program <strong>rb2colorname.py</strong>
   (as stored in GitHub)
   is constructed partly by running the <strong>rbgcsv2array.py</strong>
   program which reads
   the <a href="#rgb_combined.csv">rbg_combined.csv</a> file.

   This is necessary because changes can occur in
   the list of color names and associated points in 3D color space.

0. Program <strong>rb2colorname.py</strong> in invoked with
   a set of 3 numbers.

0. The numpy functions identify the nearest neighbor to the array input,
   and return 3 numbers.

0. The 3 numbers returned is used to lookup the
   name of the color and its Hex code (and later, its HCL code).

0. That information is returned to the caller.


## Design alternatives #

The pandas library for Python
http://pandas.pydata.org/

http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.from_csv.html

can load a Dataframe from the csv file.

<pre>
df = DataFrame.from_csv(rgb_combined.csv', sep='\t')
array = df.values # the array you are interested in
</pre>

<a name="rbg_combined.csv"></a>

## rbg_combined.csv

Column name text in the heading line begin with an underline
so each sorts to the top during sorts.

Column "_Hex" is the Hexadecimal combination of 3 RGB() hex of 2 characters each.
The column contains a leading dash because of the bad way Microsoft Excel handles hex numbers.
The conversion to hex was done using this Excel formula:

   =concatenate("#",DEC2HEX(B678,2),DEC2HEX(C678,2),DEC2HEX(D678,2))

   The single # (hash mark) makes Excel see the six-characters as text rather than numbers.

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

   There is a doubling of gray/grey color name lines due to this
   differentiation.

Column "_SVG" is used to designate names in SVG. Color numbers differs between SVG and X11 for
"gray", "gray", "green", "maroon" and "purple".
These exceptions have "diff" in X11 lines.
SVG has "darkgray" while X11 does not.

   * "SVG" is from https://www.w3.org/TR/SVG/types.html#ColorKeywords

Additional columns may be added because there are other color names, such as:

   * Pantone (proprietary).

   * https://en.wikipedia.org/wiki/Crayola#Colors
