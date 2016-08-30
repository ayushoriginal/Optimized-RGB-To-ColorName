#!/usr/bin/env python
# rgbcvs2colorarray.py
# by wilsonmar@gmail.com
# Usage: rgbcvs2colorarray.py  rgb_combined.csv
# Oputput: A = array([[222,43,221],[2,11,222], ... ])
# Open resulting file rgb_colorarray.py and paste into rgb2colorname.py


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
      file_in = 'rgb_combined_v01.csv'

# Exit if file_in not found:
if os.path.exists(file_in) and os.access(file_in, os.R_OK):
    import csv, time
    with open(file_in, 'rU') as f:
        reader = csv.reader(f, delimiter=',')
        for i in reader:
            print '# '+time.strftime('%Y-%m-%d-%H:%M (local time)')+" "+sys.argv[0]+' START: outrowcount='+ str( sum(1 for _ in f) ) +'.'
else:
    print '# '+time.strftime('%Y-%m-%d-%H:%M (local time)')+' '+sys.argv[0]+" ABORTED. Either file "+file_in+" is missing or is not readable."
    exit(2)

# Provide default file_out name argument if not provided:
if __name__ == "__main__":
#def main(argv):
   try:
      arg1 = sys.argv[2]
      file_out = sys.argv[2]
   except IndexError: # getopt.GetoptError:
   	  # Name output file by appending .txt to the name:
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
    # Print header:
    print "A = np.array([ \\" 
    # Loop through lines in input to generate: "[222,43,221],[2,11,222]", one for each color:
    rownum=0
    for i in reader:
      if rownum ==0:
        # print first row without a comma:
          print '['+i[1]+','+i[2]+','+i[3]+',"'+i[4]+'","'+i[0]+'"] \\'
          rownum=rownum+1
      else:
         print ',['+i[1]+','+i[2]+','+i[3]+',"'+i[4]+'","'+i[0]+'"] \\'
         
    # Lastly:
    print "])"
  # print "], np.int32)"



# Close the file every time:
sys.stdout.close()

sys.stdout = stdout # Restore regular stdout.
# End timer:
elapsed = timeit.default_timer() - start_time
print "# "+ time.strftime('%Y-%m-%d-%H:%M (local time)') +' '+ sys.argv[0] +" END: ran for "+ "{:.2f}".format(elapsed * 1000 )+ ' secs.'
