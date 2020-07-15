import sys

def doSomething(blobs, pattern):
    counterList = []
    answer = ""
    for element in blobs:
        if len(pattern) != 0:
            counterList.append(countPatternOccurrence(element, pattern))
        else:
            counterList.append(0)
    for counts in counterList:
        answer = answer + str(counts) + "|"
    answer = answer + str(sum(counterList))
    return answer
    
    
def countPatternOccurrence(blob, pattern):    
    counter = 0
    for i in range(len(blob) - len(pattern) + 1): 
        if (blob[i:i+len(pattern)] == pattern): 
            counter+= 1
    return counter
       
for line in sys.stdin:
    splitted_input = line.split(';')
    pattern = splitted_input[0]
    blobs = splitted_input[1].split('|')
 
    result = doSomething(blobs, pattern)
    print(result)