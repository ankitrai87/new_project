import csv
c=open('stream_payment.csv')
b=open('batch_payment.csv')
rec2_list=[]
rec3_list=[]
s_p=csv.reader(c)
b_p=list(csv.reader(b))
for row in s_p:
	for row2 in b_p:
		if row[1] in row2[1]:
			rec2_list.append(row2[2])
	for row3 in rec2_list:
		for row4 in b_p:
			if row3 in row4[1]:
				rec3_list.append(row4[2])
	
	if row[2] in rec2_list or row[2] in rec3_list:
		print "trusted"
	else:
		print "unverified"
	rec2_list=[]
	rec3_list=[]
	
	
b.close()
c.close()