""" 
Write a program to implement Round Robin Scheduling with arrival time (quantum 2 ns).
"""

from prettytable import PrettyTable


TIME = 0
processes = []
ID = 0
quantum = 2

table = PrettyTable()
table.field_names = ["Process", "Burst Time", "Arrival Time", "Waiting Time", "Turn-around Time", "Completion Time"]


class Process:
    def __init__(self, id, burst, arrival):
        self.id = id
        self.burstTime = burst
        self.remainingTime = burst
        self.arrivalTime = arrival
        self.waitingTime = int()
        self.turnAroundTime = int()
        self.completionTime = int()

    def updateRemainingTime(self, quantum):
        self.remainingTime -= quantum
        if self.remainingTime < 0:
            self.remainingTime = 0

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
    processes.sort(key=(lambda x:[x.arrivalTime, x.burstTime]))


def sortProcessesOnId():
    global processes
    processes.sort(key=lambda x: x.id)


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


def executeProcesses(quantum):
    global processes, TIME
    completedProcesses = []
    waitingProcesses = [processes[0]]
    
    while len(waitingProcesses) > 0:
        curProcess = waitingProcesses[0]
        if curProcess in processes:
            processes.remove(curProcess)
        TIME += (quantum if curProcess.remainingTime >= quantum else curProcess.remainingTime)
        curProcess.updateRemainingTime(quantum)

        waitingProcesses = waitingProcesses + [process for process in processes if process.arrivalTime <= TIME and process not in waitingProcesses]
        if curProcess.remainingTime == 0:
            curProcess.setCompletionTime(TIME)
            curProcess.setTurnAroundTime()
            curProcess.setWaitingTime()
            completedProcesses += [curProcess]
            waitingProcesses.remove(curProcess)
        else:
            waitingProcesses.append(curProcess)
            waitingProcesses.remove(curProcess)

    processes = completedProcesses


def main():
    global quantum
    N = int(input("Enter the number of processes: "))
    print()

    for i in range(N):
        createProcess()
    sortProcesses()
    executeProcesses(2)
    sortProcessesOnId()
    printProcesses()


main()