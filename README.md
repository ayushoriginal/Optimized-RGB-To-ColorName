# Optimized RGB-To-ColorName API
## Authors- Wilson Mar, Ayush Pareek

### TL;DR- Not all colours present in the physical world have an exact representation in different forms of digital spectrum and platforms. Artists, E-commerce websites, Companies etc. desire precision while publishing their work, products and logos. Some colors may not be reproducible on monitors and on printers in pigments available. This API gives closest approximation of an RGB value to a set of colour names. Its highly optimized for performance and scalibility.

![0](http://i.imgur.com/iT79E5u.png)

##Hosted at :- https://algorithmia.com/algorithms/wilsonmar/RGB2ColorName


This API makes it easier for artists to identify color names to use English words to describe colors. 
Colors are defined by 3 integers for RGB (Red Green Blue). The program returns black if any number is larger than the 255 maximum value for each color. The 256x256x256 = 16,777,216 possible individual color values.

![yo](http://i.imgur.com/f0f3IUu.png)

Currently, this API knows about 2,790 unique color names widely defined publicly. 

The three dimensions involved in specifying a color makes it difficult to manually identify the closest point with a color name.

The bulk of the work on this API was in compiling the color names and their RGB coordinates. There were many duplicates in both names and color coordinates.

##Inputs and Outputs:
The colors of a few famous social media and tech companies are known by this API, thanks to https://www.materialui.co/socialcolors. Additional companies have been added into this API, such as Google, Amazon, and IBM.


###Example 1: IBM Blue and Hex equivalent
Organizations need to precisely specify the colors in their logo so that vendors accurately render it online, in packaging, etc.. 

In https://www-03.ibm.com/press/us/en/photo/20190.wss IBM defines the color of its trademark Blue color as "PMS 2718C; Process equivalent: Cyan 75%, Magenta 43%, Yellow 0%, Black 0%; RGB equivalent: Red 90, Green 135, Blue 197; Broadcast equivalent: Red 22%, Green 42%, Blue 70%.: Let's see if this API recognizes it:

![1](http://i.imgur.com/2xMe1p1.png)


"#5A87C5" is the hex equivalent of the RGB color found.

"(+0,+0,+0)" means that the color found is a direct hit of the color input.


###Example 2: Pantone

So for many years, designers make use of the Pantone palette of 1,340 colors, which are proprietary because of the work that went into figuring out what mix of pigments of paints and dyes are needed to duplicate it accurately. 

Pantone's "PMS" colors are from http://us.labelpartners.com/pantone_coated_table.html.

For a fee, Pantone offers tools pros use to specify and measure a wide number of colors, such as "the world's ugliest color" Pantone 448 C at ["74","65",42"], which governments use to discourage smoking. 


###Example 3: X11, SVG, CSS


The X11 and SVG standards were created to name colors that can best be displayed by display monitor hardware with minimal processing (at a time when displays had a smaller gamut than today). 

![2](http://i.imgur.com/W2qN6bN.png)
![3](http://i.imgur.com/1lDCTvK.png)

####Credits:
The bulk of the work on this is to reconcile duplicate colors and color names from a variety of sources. 

19 "Metro" colors are defined by Microsoft for Windows 8 from https://www.materialui.co/metrocolors
18 Material Flat colors from https://www.materialui.co/flatuicolors
29 Company colors from https://www.materialui.co/socialcolors
Crayola colors
US Federal Standard 595 from http://www.fed-std-595.com/FS-595-Paint-Spec.html
Thanks to Ayush Pareek for his Python numpy genius.

This capability is also needed for a finger camera (IoT device) which speaks the color name.

####Tags-
accessibility
color
color palette
data transformation
mapping
python

---------------------------------------------------------------------------------------------------------------------------------------

## DESIGN AND WORKING STRUCTURE

![4](http://i.imgur.com/BmUGWRn.png)

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

   * Pantone (proprietary).

   * https://en.wikipedia.org/wiki/Crayola#Colors



Column "_SVG" is used to designate names in SVG. Color numbers differs between SVG and X11 for
"gray", "gray", "green", "maroon" and "purple".
These exceptions have "diff" in X11 lines.
SVG has "darkgray" while X11 does not.

   * "SVG" is from https://www.w3.org/TR/SVG/types.html#ColorKeywords

   "diff" is in the column if it's different than X11.

   * "duo" is noted for where there are two color names for the same color, 
   such as "aqua" and "cyan"; "fuchia" and "magenta". 
   The first of names alphabetically is returned.

TOOL NOTE: To remove diacritical (Non-ASCII) characters from a file, consider:
http://utils.paranoiaworks.org/diacriticsremover/

   * <a target="_blank" href="http://us.labelpartners.com/pantone_coated_table.html">Pantone</a> (proprietary).

Other ideas for Alogrithmia:
http://textmechanic.com/text-tools/numeration-tools/online-tally-counter/


## Design alternatives #

0. Add more color name sources (Sherwin Williams, etc.) - visit Home Depot

0. Load csv file as Dataframe - the pandas library for Python
   http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.from_csv.html


<pre>
df = DataFrame.from_csv(rgb_combined.csv', sep='\t')
array = df.values # the array you are interested in
</pre>

Columns can be removed within the program using this call:

<pre>
 RGB= np.delete(A, np.s_[3:5], axis=1) # remove columns 3 to 5.
</pre>

Based on https://algorithmia.com/algorithms/deeplearning/CaffeNet/edit

Consider https://github.com/spotify/annoy/ for sharing memory.


## Clean-up #

Please remove these intermediate attempts:

* rgb2nearestvalue.py
* rgb_color_k_nearest.py
* rgb2color_runtime_error.py
* rgb2nearestcolor.py
* rgbcsv2array.py
