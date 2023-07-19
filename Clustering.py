import random
import math

values = [43,-111,0,89,23, -1, 67, 4, -4 ] #user should put in points here
valuesY = [10, -29, 14, -7, 20, -75, 22, -65, 12] #user should put in points here
def min_val(values):
    min = values[0]
    for i in range (len(values)):
        if values[i] < min:
            min = values[i]
            
    return min

#print(min_val(values))

def max_val(values):
    max = values[0]
    for i in range(len(values)):
        if values[i] > max:
            max = values[i]
            
    return max

#print(max_val(values))

def min_index(values):
    min = 9999999999
    index = 0
    for i in range (len(values)):
        if values[i] < min:
            min = values[i]
            index = i
            
    return index

#print(min_index(values))

def max_index(values):
    max = -9999999
    index = 0
    for i in range(len(values)):
        if values[i] > max:
            max = values[i]
            index = i
            
    return index

#print(max_index(values))

def asc(values):
    values2 = []
    for i in range(len(values)):
        values2.append(min_val(values))
        values.pop(min_index(values))
        
    return values2

#print(asc(values))

def desc(values):
    values2 = []
    for i in range(len(values)):
        values2.append(max_val(values))
        values.pop(max_index(values))
        
    return values2

#print(desc(values))

def distance(values):
    distance = 999999
    for i in range(len(values)-1):
        if values[i] - values[i+1] < distance:
            distance = abs(values[i] - values[i+1])         

    return distance

#print(distance(asc(values)))

def newlist(values):
    for i in range(len(values)):
        values[i] = [values[i]]
    return values
#print(newlist(values))

def dist_index(values):
    distance = 999999
    index1 = 0
    index2 = 0
    for i in range(len(values)-1):
        if abs(values[i] - values[i+1]) < distance:
            distance = abs(values[i] - values[i+1])
            index1 = i
            index2 = i+1
    return index1,index2
#print(dist_index(asc(values)))
def average(values):
    sum = 0
    for i in range (len(values)):
        sum = sum + values[i]
    return sum/(len(values))

def hierarchical(values):
    values = newlist(values)
    for i in range(4): #4 is the number of clusters i want
        averagelist = []
        for i in range(len(values)):
            averagelist.append(average(values[i]))
        index1 = dist_index(averagelist)
        index2 = index1[1]
        values[index1[0]] += values[index2]
        values.pop(index2)
    return values

#print(hierarchical(asc(values)))

def K1D(values,k):
    move = False
    centroids = []
    oldlist1 = []
    oldlist2 = []
    oldlist3 = []
    orglist = [oldlist1, oldlist2, oldlist3]
    centroids = random.sample(range(values[0],values[-1], 1), k)
    for w in range(5):
        centroid1 = []
        centroid2 = []
        centroid3 = []
        points = [centroid1, centroid2, centroid3]
        print(centroids)
        for a in range(len(values)):
            deviation = []
            for i in range(k):
                deviation.append(abs(centroids[i]-values[a]))
            for v in range(len(deviation)):
                if min_index(deviation) == v:
                    points[v].append(values[a])
                    break
        for g in range(len(centroids)):
            if len(points[g]) > 0:
                centroids[g] = average(points[g])
        if ((points[0] == orglist[0]) & (points[1] == orglist[1]) & (points[2] == orglist[2])):
            move = True
        print(points)
        if move:
            break
        orglist = points
    
#K1D(asc(values),3) #wanted 3 centroids
def average2(values):
    sumX = 0
    sumY = 0
    for i in range (len(values)):
        sumX = sumX + values[i][0]
        sumY = sumY + values[i][1]
    return sumX/(len(values)), sumY/(len(values))

def K2D(valuesX, valuesY, k):
    move = False
    centroids = []
    oldlist1 = []
    oldlist2 = []
    oldlist3 = []
    values = []
    orglist = [oldlist1, oldlist2, oldlist3]
    for p in range(len(valuesY)):
        values.append([valuesX[p], valuesY[p]])
    for i in range(k):
        centroids.append(random.sample(range(valuesY[0],valuesY[-1], 1), 2))
    print(centroids)
    for w in range(5):
        centroid1 = []
        centroid2 = []
        centroid3 = []
        points = [centroid1, centroid2, centroid3]
        print(centroids)
        for a in range(len(values)):
            deviation = []
            for i in range(k):
                deviation.append(math.sqrt((centroids[i][0] - valuesX[a])**2 + (centroids[i][1] - valuesX[a])**2))
            for v in range(len(deviation)):
                if min_index(deviation) == v:
                    points[v].append(values[a])
                    break
        for g in range(len(centroids)):
            if len(points[g]) > 0:
                centroids[g] = average2(points[g])
        if ((points[0] == orglist[0]) & (points[1] == orglist[1]) & (points[2] == orglist[2])):
            move = True
        print(points)
        if move:
            break
        orglist = points
        
#K2D(asc(values), asc(valuesY), 3)
