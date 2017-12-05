import random
unsorted = random.sample(range(100), 10)
length = len(unsorted)
print('unsorted: ' + str(unsorted))
sorted = []

def bubbleSort():
    for pos, val in enumerate(unsorted):
        if pos == (len(unsorted)-1):
            sorted.insert(0, unsorted.pop())
            if len(sorted) != length:
                bubbleSort()
            else:
                print('sorted: ' + str(sorted))
                input()
                exit()

        if val > unsorted[pos+1]:
            unsorted[pos] = unsorted[pos+1]
            unsorted[pos+1] = val

bubbleSort()

