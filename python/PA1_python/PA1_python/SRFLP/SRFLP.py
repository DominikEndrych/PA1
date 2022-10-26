from dis import dis
import itertools as it
import multiprocessing as mp
import numpy as np
import os

def LoadFile(filename):
    dataset = {}
    file = open(filename, 'r')

    # Read 1. line
    dataset['dim'] = (int(file.readline()))    
    
    # Read 2. line
    line = file.readline()
    line.strip()
    line = line.split()
    print(line)
    dataset['widths'] = [int(w) for w in line]

    # Read rest of the file
    distances = []
    while True:
        line = file.readline()
        line = line.split()
        distances.append([int(d) for d in line])
        if not line:
            dataset['dist'] = distances
            break
    
    file.close()
    return dataset

def SRFLP(permutation, dataset):
    result = 0
    n = dataset['dim']
    for i in range(0, n-1):
        a = min(permutation[i], permutation[i+1])
        b = max(permutation[i], permutation[i+1])
        result += ( dataset['dist'][a][b] * Distance(a,b,dataset['widths']) )
    return result


def Distance(p1, p2, widths):
    sum = 0
    for i in range(min(p1, p2), max(p1, p2)+1):
        sum += widths[i]
    sum += (widths[p1] + widths[p2]) / 2
    return sum

if __name__ == '__main__':
    filename = "Y-10_t.txt"
    data = LoadFile(filename)       # Read data from file

    # Testing values
    permutation = (0,1,2,3,4,5,6,7,8,9)
    print(SRFLP(permutation, data))
