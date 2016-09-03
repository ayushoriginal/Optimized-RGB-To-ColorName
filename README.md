The program <strong>rgb2colorname.py</strong>
invokes an algorithm that identifies the name of a color closest to an RGB value provided as input.

* Input: ["221","185","135"] are RGB (Red Green Blue) values between 0 - 256.

   Alternative HCL representations are processed by another API.

* Output: Nearest color name to input RGB [221, 183, 134] is "burlywood" #DEB887 [222 184 135]

   TODO: Perhaps also return the 3 distances to the input.
   
   And an accuracy score, which is always 100% since the calculation is done mathematically.

## Usage Expected #

The utility is expected to enable artists to 
more accurately specify the color of their works in
text search engines within Google, Instagram, Etsy, Amazon, Walmart, Jet, and other 
ecommerce site so that others can better match artwork to their design intentions.

However, this may not see much use as many words in the color names 
have different associations in different parts of the world.
And artists probably desire more precision in color names than the 571 colors
in the gamut.

And some colors may not be reproducible on printers and in pigments available.

Nevertheless, this is a fun exercise for us to demonstrate use of Python features:

   * numpy library's closest-neighbor functions
   * definition of arrays and dictionary for stand-alone data values (no external dependencies)
   * calculate hex from decimal
   * string lookup in dictionary
   * naming conventions and documentation for teamwork

All different techniques were used in
https://algorithmia.com/algorithms/vagrant/snapToMaterial/edit

We are also using this exercise to demostrate our ability to 
incorporate algorithms into Algorthmia. Specifically at
<a target="_blank" href="https://algorithmia.com/algorithms/wilsonmar/RGB2ColorName">
https://algorithmia.com/algorithms/wilsonmar/RGB2ColorName</a>
(a private service during development).

Building on this achievement will be more distruptive tools such as
identify colors that are printable by specific printers,
VR to help visualize 3D color spaces, and 
ML outputs that recognize colors with more accuracy.


## Processing #

0. The 3-dimensional array in the program <strong>rgb2colorname.py</strong>
   (as stored in GitHub)
   is constructed by running the <strong>rbgcsv2array.py</strong>
   program (also in this GitHub), which reads
   the <a href="#rgb_combined.csv">rbg_combined_v01.csv</a> file.

   This is necessary because changes can occur in
   the list of color names and associated points in 3D color space.

   * http://docs.scipy.org/doc/numpy/reference/arrays.ndarray.html
   * http://docs.scipy.org/doc/numpy/reference/generated/numpy.genfromtxt.html

0. The array generated is pasted into program <strong>rgb2colorname.py</strong>.

0. Program <strong>rgb2colorname.py</strong> in invoked with an array.
   a set of 3 RGB numbers plus the hex equivalent and the color name title.

0. The numpy functions identify the nearest neighbor to the array input,
   and return 3 numbers.

0. The 3 numbers returned is used to calculated the hex code.
   
0. The hash code is used to lookup the
   name of the color (and later, its HCL code).

0. Information associated with the color found
   (RGB numbers, hex code, color name)
   is returned to the caller.


<a name="rbg_combined.csv"></a>

## rbg_combined.csv

This work draws on prior work by Wilson Mar on colors at
http://wilsonmar.com/1colors.htm#ColorNamez

Column name text in the heading line begin with an underline
so each sorts to the top during sorts.

Column "_Hex" is the Hexadecimal combination of 3 RGB() hex of 2 characters each.
The column contains a leading dash because of the bad way Microsoft Excel handles hex numbers.

The single # (hash mark) makes Excel see the six-characters as text rather than numbers.

The conversion to hex #5A87C5 was done using this Excel formula:

   <pre>
   =concatenate("#",DEC2HEX(B678,2),DEC2HEX(C678,2),DEC2HEX(D678,2))
   </pre>

To convert to hex can be done using this Excel formula:

   <pre>
   =concatenate(HEX2DEC(MID(A2,2,2))
   </pre>


Column "_Title" contains color names that in "Title" case,
with a capitalize first letters of every word.
SVG has names in all lower case.

Column "_Name" are dashes between compound words for X11.

Column "_Gray" contains either "gray" or "grey" to differentiate then alternate spellings.
X11 is defined with both, so it doubles the number of colors defined as gray/grey.

   Since we are using the colors as a look-up, we should only have one.

   "Grey" is used in Great Britain and areas that use UK English.
   "Gray" is used primarily in the United States and other areas that use US English. 
   So we only have "Gray" in this program to avoid
   doubling of gray/grey color name definitions.

Column "_seq" sequences conflicting _Hex codes.
A color has "1" in this field if it has no conflicts.
This is the only color put in the array and dictionary.
Conflicting colors are given "2", "3", etc. so they are not lost for future use.

This field is used as the secondary soft after _Hex.

   A number must be used because Excel sorts blanks under cells with values
   (the opposite of how databases do sorting).

Column "_Source"

   * "X11" is from https://en.wikipedia.org/wiki/X11_color_names
   X11 color names first defined in 1985.

   * https://cgit.freedesktop.org/xorg/app/rgb/tree/rgb.txt

   * "duo" is noted for where there are two color names for the same color, 
   such as "aqua" and "cyan"; "fuchia" and "magenta". 
   The first of names alphabetically is returned.

Column "_SVG" is used to designate names in SVG. Color numbers differs between SVG and X11 for
"gray", "gray", "green", "maroon" and "purple".
These exceptions have "diff" in X11 lines.
SVG has "darkgray" while X11 does not.

   * "SVG" is from https://www.w3.org/TR/SVG/types.html#ColorKeywords


## Design alternatives #

Additional columns may be added because there are other color names, such as:

   * <a target="_blank" href="http://us.labelpartners.com/pantone_coated_table.html">Pantone</a> (proprietary).

   * https://en.wikipedia.org/wiki/Crayola#Colors

The pandas library for Python
http://pandas.pydata.org/

http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.from_csv.html

can load a Dataframe from the csv file.

<pre>
df = DataFrame.from_csv(rgb_combined.csv', sep='\t')
array = df.values # the array you are interested in
</pre>

Columns can be removed within the program using this call:

<pre>
# RGB= np.delete(A, np.s_[3:5], axis=1) # remove columns 3 to 5.
</pre>

# Based on https://algorithmia.com/algorithms/deeplearning/CaffeNet/edit
# Consider https://github.com/spotify/annoy/ for sharing memory.


## Clean-up #

Please remove these intermediate attempts:

* rgb2nearestvalue.py
* rgb_color_k_nearest.py
* rgb2color_runtime_error.py
* rgb2nearestcolor.py
* rgbcsv2array.py
