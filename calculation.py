#! /usr/bin/python
received = 0.0
sent = 0.0
sent_time = [0,0,0]
delay = 0.0
with open("log.txt", "r") as f:
    for line in f:
        if "sent" in line:
            sent = sent + 2
            if "from node 1" in line:
                sent_time[0] = float(line[51:61])
            if "from node 2" in line:
                sent_time[1] = float(line[51:61])
            if "from node 3" in line:
                sent_time[2] = float(line[51:61])
        if "received" in line:
            received = received + 1
            if "from node 1" in line:
                delay = delay + (float(line[69:79]) - sent_time[0])
            if "from node 2" in line:
                delay = delay + (float(line[69:79]) - sent_time[1])
            if "from node 3" in line:
                delay = delay + (float(line[69:79]) - sent_time[2])

print("Packet Loss Rate: ")
print(1 - received / sent)
print("Average Time Delay")
print(delay/received)
