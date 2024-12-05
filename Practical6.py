def fcfs_scheduling(processes, arrival_times, burst_times):
    n = len(processes)  # Total kitne processes hain
    completion_times = [0] * n  # Har process ka completion time store karne ke liye
    turnaround_times = [0] * n  # Har process ka turnaround time store karne ke liye
    waiting_times = [0] * n  # Har process ka waiting time store karne ke liye

    # Completion time calculate karna
    completion_times[0] = (
        arrival_times[0] + burst_times[0]
    )  # Pehla process ka completion time
    for i in range(1, n):
        completion_times[i] = (
            max(completion_times[i - 1], arrival_times[i]) + burst_times[i]
        )

    # Turnaround aur Waiting time calculate karna
    for i in range(n):
        turnaround_times[i] = completion_times[i] - arrival_times[i]  # Turnaround time
        waiting_times[i] = turnaround_times[i] - burst_times[i]  # Waiting time

    # Results print karna
    print("Process\tArrival\tBurst\tCompletion\tTurnaround\tWaiting")
    for i in range(n):
        print(
            f"{processes[i]}\t{arrival_times[i]}\t{burst_times[i]}\t{completion_times[i]}\t\t{turnaround_times[i]}\t\t{waiting_times[i]}"
        )

    # Average calculate karna
    avg_turnaround_time = sum(turnaround_times) / n  # Turnaround ka average
    avg_waiting_time = sum(waiting_times) / n  # Waiting ka average
    print(f"\nAverage Turnaround Time: {avg_turnaround_time:.2f}")
    print(f"Average Waiting Time: {avg_waiting_time:.2f}")


# Input example
processes = ["P1", "P2", "P3", "P4"]
arrival_times = [0, 2, 4, 5]
burst_times = [7, 4, 1, 4]

# Function ko call karna
fcfs_scheduling(processes, arrival_times, burst_times)
