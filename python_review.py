import random as rnd

temperatures = []
highest_temp = 0
lowest_temp = 50
total_sum = 0
highest_temp_day = ""
lowest_temp_day = ""
days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

for i in range(7):
    temperatures.append(rnd.randrange(26, 41))

good_days_count = 0
for i in range(len(temperatures)):
    total_sum += temperatures[i]
    if temperatures[i] % 2 == 0:
        good_days_count += 1
        print(temperatures[i])
    if temperatures[i] > highest_temp:
        highest_temp = temperatures[i]
        highest_temp_day = days_of_the_week[i]
    if temperatures[i] < lowest_temp:
        lowest_temp = temperatures[i]
        lowest_temp_day = days_of_the_week[i]

avg_temp = total_sum / len(temperatures)

above_avg_days = []
for i in range(len(temperatures)):
    if temperatures[i] > avg_temp:
        above_avg_days.append(days_of_the_week[i])

for i in range(len(temperatures)):
    print(days_of_the_week[i] + ": " + str(temperatures[i]))
print("Good days count:", good_days_count)
print("Highest temperature:", highest_temp, "Highest temperature day:", highest_temp_day)
print("Lowest temperature:", lowest_temp, "Lowest temperature day:", lowest_temp_day)
print("Average temperature:", avg_temp)
for day in above_avg_days:
    print("Days above average:", day)


def bubbleSort(array):
    
  for i in range(len(array)):

    for j in range(0, len(array) - i - 1):

      
      if array[j] > array[j + 1]:

       
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp

sortedtemp=[]
sortedtemp=bubblesort(temperatures)
for i in range sortedtemp:
    print(sortedtemp[i])
