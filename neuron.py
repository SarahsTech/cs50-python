# simulate a neuron over time and count spikes.

import random

# define a function called simulate_neuron with two inputs:
# how many time steps to run and what voltage threshold causes a spike.
def simulate_neuron(steps, threshold):
    voltage = 0
    spike_count = 0

    # repeat the following code steps times.
    for t in range(steps):

        # generate a random number between 0 and 1 - simulates a noisy input to the neuron.
        input_current = random.random()
        # add that input to the neuron's voltage.
        voltage += input_current

        # check if neuron has reached firing threshold.
        if voltage >= threshold:
            # if yes, increase spike counter.
            spike_count += 1
            # reset voltage after firing.
            voltage = 0
    
    # after the loop finishes, give back the total number of spikes.
    return spike_count

# 1000 time steps, threshold of 1.5
spikes = simulate_neuron(1000, 1.5)
print("Total spikes:", spikes)