import csv
import time
import operator
import boto3

for i in xrange(1,20):
	in_f = open('/tmp/s3/saved_' + str(i) + '.txt','rU')
	reader = in_f.read()
	reader = reader.split('\t')
	s3 = boto3.client('s3')
	bucket = 'awb.prod.us-east-1.awbna'
	print "Start"
	for row in reader:
		copy_source = {'Bucket': bucket, 'Key': row}
		newKey = row[0:35] + 'impressions/' + row[35:]
		s3.copy(copy_source, bucket, newKey)
	in_f.close()
	print "-----------status---------    " + i

