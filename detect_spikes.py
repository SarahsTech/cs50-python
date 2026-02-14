import csv

# A beginner friendly script that reads voltage data from a csv file (spikes.csv)
# and prints out the voltage over time.
# This simulates the process of mointoring a neuron's electrical activity, as with computational neuroscience.
# Later, I could add logic to detect when a neuron "spikes" (fires on action potential)
# For example, when voltage becomes less negative (above a certain threshold)


# opens spikes.csv file which contains time and voltage data
with open ("spikes.csv", newline="") as file:
    # create a rader that treats each row like a dictionary
    # each row will have keys: 'time' and 'voltage'
    reader = csv.DictReader(file)
    # loop through each row of the csv file
    for row in reader:
        # print the time and voltage for each reading
        # this helps me see the voltage changes over time
        print(f"{row['time']}: {row['voltage']}")