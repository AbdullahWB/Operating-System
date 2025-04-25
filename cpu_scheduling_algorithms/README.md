# Process Scheduling Simulator
## This project implements a process scheduling simulator that compares the First-Come-First-Serve (FCFS) and Shortest Job First (SJF) scheduling algorithms. It reads process data from a file (sjfInput.txt), creates process objects, applies both scheduling algorithms, and outputs the waiting time and turnaround time for each process.
Overview
The simulator:

Reads a list of processes from sjfInput.txt, where each line specifies a process with its process ID (pid), arrival time, and burst time.
Creates Process objects with attributes like pid, arrival_time, burst_time, waiting_time, and turnaround_time.
Applies FCFS and SJF scheduling algorithms (implemented in separate FCFS.py and SJF.py modules) to compute:
Waiting Time: Time a process waits in the queue before execution.
Turnaround Time (TaT): Total time from arrival to completion (waiting time + burst time).


Prints the results for each process under both algorithms.

Scheduling Algorithms
First-Come-First-Serve (FCFS)

Description: FCFS is a non-preemptive scheduling algorithm where processes are executed in the order of their arrival time. The process that arrives first is executed first, regardless of its burst time.
Behavior: Processes are queued based on arrival_time. If multiple processes arrive at the same time, they are processed in order of pid (or queue order).
Pros:
Simple to implement.
Fair in terms of arrival order.


Cons:
Can lead to high waiting times for processes with short burst times if a long process arrives first (convoy effect).


Example: For processes arriving at t=0, t=1, t=2, FCFS executes them in that order, even if later processes have shorter burst times.

Shortest Job First (SJF)

Description: SJF is a non-preemptive scheduling algorithm that selects the process with the shortest burst time among those that have arrived at the current time. It minimizes average waiting time by prioritizing shorter jobs.
Behavior: At each time step, SJF checks all processes that have arrived and picks the one with the smallest burst_time. If multiple processes have the same burst time, the one with the earliest arrival time (or lowest pid) is chosen.
Pros:
Optimizes average waiting time.
Efficient for systems with varied burst times.


Cons:
Requires knowledge of burst times in advance.
Can starve long-running processes if short jobs keep arriving.


Example: If processes with burst times 10, 5, and 2 arrive at t=0, SJF executes the process with burst time 2 first.

Code Structure
The main script (scheduler.py, or similar) performs the following:

Defines a Process class to represent each process with attributes:
pid: Process ID (unique identifier).
arrival_time: Time the process arrives in the system.
burst_time: Time required to complete the process.
remaining_time: Tracks remaining execution time (equals burst_time initially).
waiting_time: Time spent waiting in the queue.
turnaround_time: Total time from arrival to completion.
priority and queue_level: Optional attributes (not used in this implementation).


Reads process data from sjfInput.txt, creating a Process object for each line.
Applies FCFS and SJF scheduling using imported fcfs and sjf functions.
Prints the waiting time and turnaround time for each process under both algorithms.
```
Main Code
from FCFS import fcfs
from SJF import sjf


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

print("\n========fcfs=========\n")
fcfsProcess = fcfs(processes)
for process in fcfsProcess:
    print(f"process{process.pid}: waiting time is {process.waiting_time}ms and TaT is {process.turnaround_time}")

print("\n========sjf=========\n")
sjfProcess = sjf(processes)
for process in sjfProcess:
    print(f"process{process.pid}: waiting time is {process.waiting_time}ms and TaT is {process.turnaround_time}")

Input File (sjfInput.txt)
The input file contains 20 processes, each on a new line, with the format pid arrival_time burst_time. The processes are designed to test FCFS and SJF with varied arrival and burst times:
1 0 8
2 0 4
3 1 6
4 1 2
5 2 10
6 2 3
7 3 5
8 3 1
9 4 7
10 4 9
11 5 3
12 5 12
13 6 4
14 6 2
15 7 8
16 7 5
17 8 6
18 8 1
19 9 10
20 9 3
```
Dependencies

FCFS.py: Contains the fcfs function, which implements the FCFS scheduling algorithm.
SJF.py: Contains the sjf function, which implements the non-preemptive SJF scheduling algorithm.
Both functions are assumed to:
Accept a list of Process objects.
Update each process’s waiting_time and turnaround_time.
Return the processed list.



How to Run

Prepare the Input File:
Create sjfInput.txt in the same directory as the script.
Copy the input data above into sjfInput.txt.


Ensure Dependencies:
Verify that FCFS.py and SJF.py are in the same directory and implement the fcfs and sjf functions.


Run the Script:python scheduler.py


Output:
The script prints each process’s details as it’s loaded.
It then shows the waiting time and turnaround time for each process under FCFS and SJF.


```
Example Output
The output matches the scheduling results for the 20 processes, showing how FCFS and SJF differ in process ordering and performance metrics.
Loading Processes
Process pid is 1: arrival time: 0, burst time: 8
Process pid is 2: arrival time: 0, burst time: 4
Process pid is 3: arrival time: 1, burst time: 6
Process pid is 4: arrival time: 1, burst time: 2
Process pid is 5: arrival time: 2, burst time: 10
Process pid is 6: arrival time: 2, burst time: 3
Process pid is 7: arrival time: 3, burst time: 5
Process pid is 8: arrival time: 3, burst time: 1
Process pid is 9: arrival time: 4, burst time: 7
Process pid is 10: arrival time: 4, burst time: 9
Process pid is 11: arrival time: 5, burst time: 3
Process pid is 12: arrival time: 5, burst time: 12
Process pid is 13: arrival time: 6, burst time: 4
Process pid is 14: arrival time: 6, burst time: 2
Process pid is 15: arrival time: 7, burst time: 8
Process pid is 16: arrival time: 7, burst time: 5
Process pid is 17: arrival time: 8, burst time: 6
Process pid is 18: arrival time: 8, burst time: 1
Process pid is 19: arrival time: 9, burst time: 10
Process pid is 20: arrival time: 9, burst time: 3

FCFS Results
FCFS processes in arrival order, leading to higher waiting times for short jobs that arrive later:
========fcfs=========

process1: waiting time is 0ms and TaT is 8
process2: waiting time is 8ms and TaT is 12
process3: waiting time is 11ms and TaT is 17
process4: waiting time is 17ms and TaT is 19
process5: waiting time is 18ms and TaT is 28
process6: waiting time is 28ms and TaT is 31
process7: waiting time is 30ms and TaT is 35
process8: waiting time is 35ms and TaT is 36
process9: waiting time is 35ms and TaT is 42
process10: waiting time is 42ms and TaT is 51
process11: waiting time is 50ms and TaT is 53
process12: waiting time is 53ms and TaT is 65
process13: waiting time is 64ms and TaT is 68
process14: waiting time is 68ms and TaT is 70
process15: waiting time is 69ms and TaT is 77
process16: waiting time is 77ms and TaT is 82
process17: waiting time is 81ms and TaT is 87
process18: waiting time is 87ms and TaT is 88
process19: waiting time is 87ms and TaT is 97
process20: waiting time is 97ms and TaT is 100

SJF Results
SJF prioritizes short jobs, reducing waiting times for processes with low burst times:
========sjf=========

process1: waiting time is 52ms and TaT is 60
process2: waiting time is 0ms and TaT is 4
process3: waiting time is 32ms and TaT is 38
process4: waiting time is 4ms and TaT is 6
process5: waiting time is 75ms and TaT is 85
process6: waiting time is 8ms and TaT is 11
process7: waiting time is 20ms and TaT is 25
process8: waiting time is 1ms and TaT is 2
process9: waiting time is 41ms and TaT is 48
process10: waiting time is 64ms and TaT is 73
process11: waiting time is 8ms and TaT is 11
process12: waiting time is 92ms and TaT is 104
process13: waiting time is 13ms and TaT is 17
process14: waiting time is 1ms and TaT is 3
process15: waiting time is 53ms and TaT is 61
process16: waiting time is 21ms and TaT is 26
process17: waiting time is 31ms and TaT is 37
process18: waiting time is 1ms and TaT is 2
process19: waiting time is 78ms and TaT is 88
process20: waiting time is 7ms and TaT is 10
```
Notes

Input File: The sjfInput.txt file must exist and contain at least 20 valid lines. If fewer lines are present, the script processes only those available.
Error Handling: The code checks for valid line formats (three integers) but could be enhanced to handle file-not-found errors or invalid data.
Assumptions:
The fcfs and sjf functions are non-preemptive and correctly update waiting_time and turnaround_time.
The input processes are designed to highlight differences between FCFS (arrival-order-based) and SJF (burst-time-based).


Extensibility: The Process class includes priority and queue_level for potential use in priority-based or multilevel queue scheduling algorithms.

Future Improvements

Add error handling for file access issues.
Implement visualization (e.g., Gantt charts) to show process execution order.
Support preemptive SJF or other scheduling algorithms (e.g., Round Robin).
Calculate and display average waiting time and turnaround time.

License
This project is for educational purposes and has no specific license. Feel free to use and modify it as needed.
