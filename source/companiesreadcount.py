#from sys import argv
#script, filename,fileoutput = argv

import csv

txt = open ('test_sample.csv','r')  #open file
out = open('outputfile.csv','w')      #write file

reader = csv.reader(txt)
writer = csv.writer(out)

id = 1
header = True
for line in reader:
	# print id
	#print line
	if header:
		writer.writerow(['ID', 'Company Name', 'Freq'])
		header = False
		continue

	if len(line) == 0:
		continue
	
	ID = 'ID' + str(id)
	writer.writerow([ID] + line)
	id += 1

txt.close()
out.close()