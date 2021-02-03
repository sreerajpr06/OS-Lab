""" 
Write a program to implement FCFS scheduling with arrival time.

Processes, Burst Time, Arrival Time, Waiting Time, Turn-Around Time, Completion Time
"""
from prettytable import PrettyTable


TIME = 0
processes = []
ID = 0

table = PrettyTable()
table.field_names = ["Process", "Burst Time", "Arrival Time", "Waiting Time", "Turn-around Time", "Completion Time"]


class Process:
    def __init__(self, id, burst, arrival):
        self.id = id
        self.burstTime = burst
        self.arrivalTime = arrival
        self.waitingTime = int()
        self.turnAroundTime = int()
        self.completionTime = int()

    def setCompletionTime(self, time):
        self.completionTime = time

    def setTurnAroundTime(self):
        self.turnAroundTime = self.completionTime - self.arrivalTime

    def setWaitingTime(self):
        self.waitingTime = self.turnAroundTime - self.burstTime


def createProcess():
    global ID, processes
    ID += 1
    id = ID
    print("Process " + str(ID))
    burst = int(input("Enter the burst time of the process: "))
    arrival = int(input("Enter the arrival time of the process: "))
    print()

    p = Process(id, burst, arrival)
    processes.append(p)


def sortProcesses():
    global processes
    processes.sort(key=(lambda x: x.arrivalTime))


def printProcesses():
    global processes, table
    avgWaitingTime = sum(process.waitingTime for process in processes) / len(processes)
    avgTurnAroundTime = sum(process.turnAroundTime for process in processes) / len(processes)

    # Processes, Burst Time, Arrival Time, Waiting Time, Turn-Around Time, Completion Time
    for process in processes:
        table.add_row([
            process.id,
            process.burstTime,
            process.arrivalTime,
            process.waitingTime,
            process.turnAroundTime,
            process.completionTime
        ])

    print(table)
    print("Average waiting time: " + str(format(avgWaitingTime, '.5f')))
    print("Average turn-around time: " + str(format(avgTurnAroundTime, '.5f')))


def sortProcessesOnId():
    global processes
    processes.sort(key=lambda x: x.id)


def executeProcesses():
    global processes, TIME

    for process in processes:
        if TIME < process.arrivalTime:
            TIME = process.arrivalTime
        TIME += process.burstTime
        process.setCompletionTime(TIME)
        process.setTurnAroundTime()
        process.setWaitingTime()


def main():
    N = int(input("Enter the number of processes: "))
    print()

    for i in range(N):
        createProcess()
    sortProcesses()
    executeProcesses()
    sortProcessesOnId()
    printProcesses()


main()