# import requests
# import json
import math

VerifyingPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73,
                   79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163,
                   167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251,
                   257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349
                   ]
FalseVerifyingPrimes = [2, 3, 5, 7, 12, 13, 17, 19, 23, 29, 31, 37, 41, 44, 47, 53, 59, 61, 67, 72, 73,
                        79, 83, 89, 97, 101, 104, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163,
                        167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251,
                        257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349
                        ]  # 12-->11, 44-->43, 72-->71, 104-->103


def DisplayPrimesInArray (start=0, offset=0, verify=False, falseData=False):
    j = 0
    testArray = FalseVerifyingPrimes if falseData else VerifyingPrimes
    for i in range(start, len(isPrime)):
        if isPrime[i]:
            if verify:
                test = str(testArray[j])
                if i+offset == testArray[j]:
                    test = ' = ' + test
                else:
                    test = ' <> ' + test + '!!!'
                print(f"{i+offset}{test},", end=" ")
            else:
                print(i+offset, end=" ")
            j += 1


def FindNewPrimeIndexInCandidateArray(start=0, offset=0):
    global foundPrimeIndex
    for i in range(start, len(isPrime)):
        if isPrime[i]:
            foundPrimes.append(i+offset)
            foundPrimeIndex += 1
            return i


def ReadOffRemainingPrimes(start=0, offset=0):
    global foundPrimeIndex
    for i in range(start, len(isPrime)):
        if isPrime[i]:  
            # foundPrimeIndex += 1  #might need to reset this index here instead of maintain
            foundPrimes.append(i+offset)


def CrossOffArrayEntries(start, end, step, doPrint=False):
    # arrLen = len(isPrime)
    # crosses = len(isPrime[start:arrLen:step])
    # isPrime[start:arrLen:step] = [False]*crosses
    print("Crossing off composites.")
    for i in range(start, end, step):
        if doPrint:
            print(i, end=" ")
        isPrime[i] = False
    if doPrint:
        print("")


upper = 135
foundPrimes = []

# def LoadArray(start,end):
isPrime = [True]*upper

topPrime = math.trunc(math.sqrt(upper))
print(f"topPrime--{topPrime}")
isPrime[0:2] = [False, False]
arrayOffset = 0 # 2

# print isPrime[0:2]
# my_list = [False for i in range(upper)]
# for i in range(len(foundPrimes)):
#    isPrime[foundPrimes[i]] = False

foundPrimeIndex = -1
currIsPrimeIndex = FindNewPrimeIndexInCandidateArray(0)
currPrime = currIsPrimeIndex # foundPrimes[foundPrimeIndex]
start = currPrime * currPrime # -arrayOffset
print(f"currIsPrimeIndex: {currIsPrimeIndex}   foundPrimeIndex: {foundPrimeIndex}   currPrime: {currPrime}   start: {start}")
print(f"foundPrimes[foundPrimeIndex: {foundPrimeIndex}]<-->{foundPrimes[foundPrimeIndex]}")
print(foundPrimes)
    
while currPrime <= topPrime:
    # currPrimeIndex * currPrimeIndex < len(isPrime):

    CrossOffArrayEntries(start, len(isPrime), currPrime)

    currIsPrimeIndex = FindNewPrimeIndexInCandidateArray(currIsPrimeIndex+1)
    currPrime = currIsPrimeIndex
    start = currPrime * currPrime # -arrayOffset
    print(f"currIsPrimeIndex: {currIsPrimeIndex}   foundPrimeIndex: {foundPrimeIndex}   currPrime: {currPrime}   start: {start}")
    print(f"foundPrimes[foundPrimeIndex: {foundPrimeIndex}]<-->{foundPrimes[foundPrimeIndex]}")
    print(foundPrimes)


ReadOffRemainingPrimes()
DisplayPrimesInArray(currPrime, 0)

print('Good job, John!!!')
#  DisplayArray()
# end-jrs
