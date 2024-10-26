# Emily Pascetta
import re
from statistics import mean, median, stdev
import sys
import matplotlib.pyplot as plt
import numpy as np


# Function to extract times from ping output
def gettimes(filename):
    times = []
    lossperiods = []
    currperiod = 0
    losses = 0
    with open(filename, 'r') as file:
        for line in file:
            # Extract times from each line
            num = re.search(r'time=(\d+)ms', line)
            if num:
                # Add each time to a list once extracted
                times.append(float(num.group(1)))
                # Update the current loss period if there is one
                if currperiod > 0:
                    lossperiods.append(currperiod)
                    # Reset the loss period
                    currperiod = 0
            elif 'Request timed out.' in line:
                # Time did not exist, add nothing to the list and increment packet losses/ current loss period
                losses += 1
                currperiod += 1
    # Return the list of times, the number of losses, and the list of loss periods
    return times, losses, lossperiods


# Function to plot CDF of times
def graphcdf(times):
    # Sort data and find the cdf (how often something happens/sample size)
    times = np.sort(times)
    cdf = np.arange(len(times)) / float(len(times))

    # Plot the graph
    plt.figure()
    plt.plot(times, cdf, marker='*', linestyle='none')
    # Labeling axis
    plt.ylabel('CDF')
    plt.xlabel('Latency (ms)')
    plt.title('CDF of Ping Latencies')
    plt.grid(True)
    plt.show()


# Main function to run the analysis
def main():
    # Get file from command line
    if len(sys.argv) < 2:
        print("No file provided")
        sys.exit(1)

    filename = sys.argv[1]
    # Get times
    times, losses, lossperiods = gettimes(filename)

    # Find stats
    if len(lossperiods) > 0:
        maxloss = max(lossperiods)
        avgloss = mean(lossperiods)
    else:
        maxloss = 0
        avgloss = 0

    mintime = min(times)
    maxtime = max(times)
    meantime = mean(times)
    mediantime = median(times)
    stddev = stdev(times)
    packetlossrate = (losses / 100) * 100

    # Print the output to the console
    print("Minimum latency: ", mintime, "ms")
    print("Maximum latency: ", maxtime, "ms")
    print("Mean latency: ", meantime, "ms")
    print("Median latency: ", mediantime, "ms")
    print("Standard deviation of latency: ", stddev, "ms")
    print(f"Packet loss rate: {packetlossrate:.2f}%")
    print("Average packet loss period: ", avgloss)
    print("Maximum packet loss period: ", maxloss)

    # Plot the CDF
    graphcdf(times)


if __name__ == "__main__":
    main()
