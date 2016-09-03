#!/usr/bin/env python
# rgbcvs2rgbarray.py
# by wilsonmar@gmail.com
# Usage: rgbcvs2colorarray.py  rgb_combined.csv
# Oputput: A = array([[222,43,221],[2,11,222], ... ])
# Open resulting file rgb_colorarray.py and paste into rgb2colorname.py

from __future__ import print_function
# Begin timer:
import timeit
start_time = timeit.default_timer()

# Get argument list using sys module:
import sys, os.path
def program(*args):
    # do whatever
    pass
# Provide default file_in name argument if not provided:
if __name__ == "__main__":
#def main(argv):
   try:
      arg1 = sys.argv[1]
      file_in = sys.argv[1]
   except IndexError: # getopt.GetoptError:
      # print "Usage: " + sys.argv[0] + ' -i <inputfile> -o <outputfile>'
      # sys.exit(2)
      file_in = 'rgb_combined_v05.csv'

# Exit if file_in not found:
if os.path.exists(file_in) and os.access(file_in, os.R_OK):
    import csv, time
    with open(file_in, 'rU') as f:
        reader = csv.reader(f, delimiter=',')
        for i in reader:
            header_rows = '# '+time.strftime('%Y-%m-%d-%H:%M (local time)')+" "+sys.argv[0]+' START: outrowcount='+ str( sum(1 for _ in f) ) +'.'
            print(header_rows)
else:
    print('# '+time.strftime('%Y-%m-%d-%H:%M (local time)')+' '+sys.argv[0]+" ABORTED. Either file "+file_in+" is missing or is not readable.")
    exit(2)

# Provide default file_out name argument if not provided:
if __name__ == "__main__": #def main(argv):
   # Name output file by appending .txt to the name:
   try:
      arg1 = sys.argv[2]
      file_out = sys.argv[2] +'.'+ file_in + '.txt'
   except IndexError: # getopt.GetoptError:
      file_out = file_in + '.txt'

# Send STDOUT to a file:
stdout = sys.stdout  # remember the handle to the real standard output.
sys.stdout=open( file_out,"w")

# Print in yml format:
import csv
# 'rU' means open in universal-newline mode needed on Macs:
#with open('./Portfolio.csv', 'rU') as f:

with open(file_in, 'rU') as f:
    reader = csv.reader(f, delimiter=',')
    first_line = f.readline() # pull out first line - do not print 
    # TODO: Remove duplicates.
    print("    RGB = np.array([",end="")
    # Loop through lines in input to generate: "[222,43,221],[2,11,222]", one for each color:
    rownum=0
    for i in reader:
      strRGB='['+i[1]+','+i[2]+','+i[3]+']'
      if rownum ==0:
        # print first row without a comma:
        print(strRGB,end="")
        lastRGB=strRGB
        rownum=rownum+1
      else:
        if lastRGB == strRGB:
           # skip the duplicate
           pass
        else:
          print(','+strRGB,end="")
          lastRGB = strRGB
          rownum=rownum+1
    print("])") # with NewLine

footer_rows="    # "+ time.strftime('%Y-%m-%d-%H:%M (local time)') +' '+ sys.argv[0] +" Output "+ str(rownum)+ ' rows.'
print(footer_rows)
# Close the file every time:
sys.stdout.close()

sys.stdout = stdout # Restore regular stdout.
# End timer:
elapsed = timeit.default_timer() - start_time
print("# "+ time.strftime('%Y-%m-%d-%H:%M (local time)') +' '+ sys.argv[0] +" END: ran for "+ "{:.2f}".format(elapsed * 1000 )+ ' secs.')
print('    '+footer_rows)