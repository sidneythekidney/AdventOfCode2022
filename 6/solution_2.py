with open('input.txt') as f:
    signal = f.readlines()[0]

for i in range(14, len(signal), 1):
    # Create a set of the items in the array
    if len(set(signal[i-14:i])) == 14:
        print("Unique char substring: " + str(i))
        break
