import csv
c=open('stream_payment.csv')
b=open('batch_payment.csv')
rec2_list=[]
rec3_list=[]
rec4_list=[]
rec5_list=[]
rec6_list=[]
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
	for row5 in rec3_list:
		for row6 in b_p:
			if row5 in row6[1]:
				rec4_list.append(row6[2])
	for row7 in rec4_list:
		for row8 in b_p:
			if row7 in row8[1]:
				rec5_list.append(row8[2])
	for row9 in rec5_list:
		for row10 in b_p:
			if row9 in row10[1]:
				rec6_list.append(row10[2])
	
	if row[2] in rec2_list or row[2] in rec3_list or row[2] in rec4_list or row[2] in rec5_list or row[2] in rec6_list:
		print "trusted"
	else:
		print "unverified"
	rec2_list=[]
	rec3_list=[]
	rec4_list=[]
	rec5_list=[]
	rec6_list=[]
	
b.close()
c.close()