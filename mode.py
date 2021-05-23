import csv 
from collections import Counter

with open('Height-weight.csv',newline = '')as f:
    reader=csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data=[]
for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_data.append(float(n_num))

#calculating mode

data = Counter(new_data)
mode_data_for_range={
    "50-60":0,
    "60-70":0,
    "70-80":0

}
for height,occourence in data.items():
    if 50<float (height)<60:
        mode_data_for_range["50-60"]+= occourence 

    elif 60<float(height)<70:
        mode_data_for_range["60-70"]+= occourence 
    elif 70<float(height)<80:
        mode_data_for_range["70-80"]+= occourence 


mode_range,mode_occourence = 0,0
for range,occourence in  mode_data_for_range.items():
    if occourence>mode_occourence   :
        mode_range,mode_occourence=[int(range.split("-")[0]),int(range.split("-")[1])],occourence
mode = float((mode_range[0]+mode_range[1])/2)
print("mode is : "+str(mode))

