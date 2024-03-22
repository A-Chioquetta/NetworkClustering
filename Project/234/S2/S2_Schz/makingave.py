import numpy as np

input_data1 = open('S2_run0Sc.dat', 'r')
input_data2 = open('S2_run1Sc.dat', 'r')
input_data3 = open('S2_run2Sc.dat', 'r')
input_data4 = open('S2_run3Sc.dat', 'r')
input_data5 = open('S2_run4Sc.dat', 'r')
# input_data6 = open('S2_run6t.dat', 'r')
# input_data7 = open('S2_run7t.dat', 'r')
# input_data8 = open('S2_run8t.dat', 'r')
# input_data9 = open('S2_run9t.dat', 'r')
# input_data10 = open('S2_run10t.dat', 'r')




values1 =[]
thresh =[]
for row in input_data1:
    columns = row.rstrip('\n').split('      ')
    T = columns[0]
    value = columns[1]
    thresh.append(float(T))
    values1.append(float(value))

values2 =[]
for row in input_data2:
    columns = row.rstrip('\n').split('      ')
    T = columns[0]
    value = columns[1]
    values2.append(float(value))




values3 =[]
for row in input_data3:
    columns = row.rstrip('\n').split('      ')
    T = columns[0]
    value = columns[1]
    values3.append(float(value))


values4 =[]
for row in input_data4:
    columns = row.rstrip('\n').split('      ')
    T = columns[0]
    value = columns[1]
    values4.append(float(value))

values5 =[]
for row in input_data5:
    columns = row.rstrip('\n').split('      ')
    T = columns[0]
    value = columns[1]
    values5.append(float(value))

# values6 =[]
# for row in input_data6:
#     columns = row.rstrip('\n').split('      ')
#     T = columns[0]
#     value = columns[1]
#     values6.append(float(value))

# values7 =[]
# for row in input_data7:
#     columns = row.rstrip('\n').split('      ')
#     T = columns[0]
#     value = columns[1]
#     values7.append(float(value))

# values8 =[]
# for row in input_data8:
#     columns = row.rstrip('\n').split('      ')
#     T = columns[0]
#     value = columns[1]
#     values8.append(float(value))
 

# values9 =[]
# for row in input_data9:
#     columns = row.rstrip('\n').split('      ')
#     T = columns[0]
#     value = columns[1]
#     values9.append(float(value))

# values10 =[]
# 
# for row in input_data10:
#     columns = row.rstrip('\n').split('      ')
#     T = columns[0]
#     value = columns[1]
#     
#     values10.append(float(value))


averages =[]
for i in range(len(values1)):
    averages.append((values1[i]+values2[i]+values3[i]+values4[i]+values5[i])/5.0) 
    with open('S2_averagesSc.dat', 'a') as file:
        file.write(str(thresh[i])+ "    "   +str(averages[i])+"\n")

# print(averages)





input_data1.close()
input_data2.close()
input_data3.close()
input_data4.close()
input_data5.close()
# input_data6.close()
# input_data7.close()
# input_data8.close()
# input_data9.close()
# input_data10.close()