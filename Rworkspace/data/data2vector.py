#!/usr/bin/python
'''
write by zhouyang@mclab
email: goat.zhou@qq.com
test on Centos7,python 2.7.5

*******************
preprocess the data
change the data to vector
I keep the symbol '?' which in original data,you can do what you
like in preprocessing the unknown values
so you can read it into matlab very easyly
*******************
'''
Workclass_list=['?','Private','Self-emp-not-inc','Self-emp-inc','Federal-gov','Local-gov','State-gov','Without-pay','Never-worked']
Education_list=['?','Bachelors','Some-college','11th','HS-grad','Prof-school','Assoc-acdm','Assoc-voc','9th','7th-8th','12th','Masters','1st-4th','10th','Doctorate','5th-6th','Preschool']

Marital_status_list=[];
Marital_status = '?,Married-civ-spouse,Divorced,Never-married,Separated,Widowed,Married-spouse-absent,Married-AF-spouse'
Marital_status_list=list(Marital_status.split(','))

Occupation_list=[]
Occupation="?,Tech-support,Craft-repair,Other-service,Sales,Exec-managerial,Prof-specialty,Handlers-cleaners,Machine-op-inspct,Adm-clerical,Farming-fishing,Transport-moving,Priv-house-serv,Protective-serv,Armed-Forces"
Occupation_list=list(Occupation.split(','))

Relationship="?,Wife,Own-child,Husband,Not-in-family,Other-relative,Unmarried"
Relationship_list=list(Relationship.split(','))

Race="?,White,Asian-Pac-Islander,Amer-Indian-Eskimo,Other,Black"
Race_list=list(Race.split(','))

Sex_list=['?','Female','Male']

Native_country_list=[]
Native_country="?,United-States,Cambodia,England,Puerto-Rico,Canada,Germany,Outlying-US(Guam-USVI-etc),India,Japan,Greece,South,China,Cuba,Iran,Honduras,Philippines,Italy,Poland,Jamaica,Vietnam,Mexico,Portugal,Ireland,France,Dominican-Republic,Laos,Ecuador,Taiwan,Haiti,Columbia,Hungary,Guatemala,Nicaragua,Scotland,Thailand,Yugoslavia,El-Salvador,Trinadad&Tobago,Peru,Hong,Holand-Netherlands"
Native_country_list=list(Native_country.split(','))
#print len(Native_country_list), len(Occupation_list),len(Marital_status_list),len(Race_list)
#attention the adult.data result is like <=50\n
#Result_list=['<=50K\n','>50K\n']
#but the adult.test result is like <=50.\n  ,have a '.'(dot)
Result_list=['<=50K.\n','>50K.\n']
Attribute=[]
for num in range(0,15):
		Attribute.append([])

Attribute[1]=Workclass_list
Attribute[3]=Education_list
Attribute[5]=Marital_status_list
Attribute[7]=Relationship_list
Attribute[6]=Occupation_list
Attribute[8]=Race_list
Attribute[9]=Sex_list
Attribute[13]=Native_country_list
Attribute[14]=Result_list

fread_id = open("adult.test",'r')
fwrite_id = open("adult.test.vector",'w')
#fwrite_err_id = open("adult.test.err",'w')

read_list=[]

for line in fread_id.readlines():
		write_list=[]
		read_list=list(line.split(', '))
#		print read_list
		write_list.append(read_list[0])
		write_list.append(read_list[2])
		write_list.append(read_list[4])
		write_list.append(read_list[10])	
		write_list.append(read_list[11])
		write_list.append(read_list[12])
		for num in [1,3,5,6,7,8,9,13]:
			temp=str(Attribute[num].index(read_list[num]))
			if temp=='0':
				write_list.append('?')
			else:
				write_list.append(temp)
		write_list.append(str(Attribute[14].index(read_list[14])))
		fwrite_id.write(','.join(write_list))
		fwrite_id.write('\n')
				


#fwrite_err_id.close()
fread_id.close()
fwrite_id.close()
