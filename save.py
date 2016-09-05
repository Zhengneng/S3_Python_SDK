import csv
import time
import operator


in_f = open('/tmp/s3/out3.txt','rU')
reader = csv.reader(in_f)

#new_rows_list  = []
string = ''


print "Start"
for row in reader:
        row = row[0][31:]
        string = string + row + '\t'


in_f.close()

out_f = open('/tmp/s3/saved2.txt','wb')
out_f.write(string)
out_f.close()

print "Done"

