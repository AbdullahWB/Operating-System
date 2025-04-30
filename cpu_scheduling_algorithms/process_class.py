from FCFS import fcfs
from SJF import sjf
from SRTF import srtf
from RR import round_robin

class Process:
    def __init__(self, pid, arrival_time, burst_time, priority=None, queue_level=None):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0
        self.priority = priority
        self.queue_level = queue_level
        

# processes = [
#    Process(pid=1, arrival_time=0, burst_time=8),
#    Process(pid=2, arrival_time=1, burst_time=4),
#    Process(pid=3, arrival_time=2, burst_time=6),
#    Process(pid=4, arrival_time=3, burst_time=9),
#    Process(pid=5, arrival_time=4, burst_time=3), 
# ]

processes = []

with open("sjfInput.txt", "r") as f:
    for line in f.readlines()[:20]:
        parts = line.strip().split()
        if len(parts) == 3:
            pid = int(parts[0])
            arrival_time = int(parts[1])
            burst_time = int(parts[2])
            processes.append(Process(pid, arrival_time, burst_time))
            print(f"Process pid is {pid}: arrival time: {arrival_time}, burst time: {burst_time}")

# print("\n========fcfs=========\n")
# fcfsProcess = fcfs(processes)

# for process in fcfsProcess:
#     print(f"process{process.pid}: waiting time is {process.waiting_time}ms and TaT is {process.turnaround_time}")
    
# print("\n========sjf=========\n")
# sjfProcess = sjf(processes)

# for process in sjfProcess:
#     print(f"process{process.pid}: waiting time is {process.waiting_time}ms and TaT is {process.turnaround_time}")

print("\n========sjf=========\n")
srtfProcess, all_time = srtf(processes)

for process in srtfProcess:
    print(f"process{process.pid}: waiting time is {process.waiting_time}ms and TaT is {process.turnaround_time}")
avg_waiting_time, avg_turnaround_time, avg_completion_time = all_time
print(f"Average Waiting Time: {avg_waiting_time:.2f}")
print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")
print(f"Average Completion Time: {avg_completion_time:.2f}")

print("\n========RR=========\n")
round_robin_Process, all_time_rr = round_robin(processes, 4)

for process in round_robin_Process:
    print(f"process{process.pid}: waiting time is {process.waiting_time}ms and TaT is {process.turnaround_time}")
avg_waiting_time, avg_turnaround_time, avg_completion_time = all_time_rr
print(f"Average Waiting Time: {avg_waiting_time:.2f}")
print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")
print(f"Average Completion Time: {avg_completion_time:.2f}")