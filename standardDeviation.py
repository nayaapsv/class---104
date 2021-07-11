import math



# list of elements to calculate mean
import csv
import statistics
with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)


data = file_data[0]

#getting the mean
# data = [20,69,56,90,40,99,86,100,70,69,80,65,57,82,90,70,79,39,90,80,86,53,97,95,88,47,100,56,97,100] #list of x or y
# data=[60,61,65,63,98,99,90,95,91,96]

# finding mean
def mean(data):
    n= len(data)
    total =0
    for x in data:
        total += int(x)

    mean = total / n
    return mean

squarelist = []

for number in data:
    a = int(number)-mean(data)
    a = a*a
    squarelist.append(a)
    
sum = 0
for i in squarelist:
    sum = sum+i

result  = sum/(len(data)-1)
sd = math.sqrt(result)
print(sd)

std = statistics.stdev(data)
print(std)