with open('input.txt') as f:
    signal = f.readlines()[0]

for i in range(4, len(signal), 1):
    # Create a set of the items in the array
    if len(set(signal[i-4:i])) == 4:
        print("Unique char substring: " + str(i))
        break
