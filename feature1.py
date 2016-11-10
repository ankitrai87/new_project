import csv
c=open('stream_payment.csv')
b=open('batch_payment.csv')
rec2_list=[]

##for row in b_p:
##	sender_1=row[1]
##	receiver_1=row[2]
s_p=csv.reader(c)
b_p=list(csv.reader(b))
for row in s_p:
	for row2 in b_p:
		if row[1] in row2[1]:
			rec2_list.append(row2[2])
	if row[2] in rec2_list:
		print "trusted"
	else:
		print "unverified"
	rec2_list=[]
b.close()
c.close()


	


			

