def sjf_scheduling(processes, arrival_times, burst_times):
    n = len(processes)  # Number of processes
    completed = [False] * n  # To track which processes are completed
    completion_times = [0] * n  # Completion times of processes
    turnaround_times = [0] * n  # Turnaround times of processes
    waiting_times = [0] * n  # Waiting times of processes

    current_time = 0  # Tracks the current time in the CPU
    completed_count = 0  # Counts how many processes are completed

    while completed_count < n:
        # Find the process with the shortest burst time among available processes
        shortest_job_index = -1
        min_burst_time = float("inf")

        for i in range(n):
            if arrival_times[i] <= current_time and not completed[i]:
                if burst_times[i] < min_burst_time:
                    min_burst_time = burst_times[i]
                    shortest_job_index = i

        if shortest_job_index == -1:  # No process has arrived yet
            current_time += 1
            continue

        # Process the shortest job
        current_time += burst_times[shortest_job_index]
        completion_times[shortest_job_index] = current_time
        turnaround_times[shortest_job_index] = (
            completion_times[shortest_job_index] - arrival_times[shortest_job_index]
        )
        waiting_times[shortest_job_index] = (
            turnaround_times[shortest_job_index] - burst_times[shortest_job_index]
        )

        completed[shortest_job_index] = True
        completed_count += 1

    # Print the results
    print("Process\tArrival\tBurst\tCompletion\tTurnaround\tWaiting")
    for i in range(n):
        print(
            f"{processes[i]}\t{arrival_times[i]}\t{burst_times[i]}\t{completion_times[i]}\t\t{turnaround_times[i]}\t\t{waiting_times[i]}"
        )

    # Calculate average turnaround and waiting times
    avg_turnaround_time = sum(turnaround_times) / n
    avg_waiting_time = sum(waiting_times) / n
    print(f"\nAverage Turnaround Time: {avg_turnaround_time:.2f}")
    print(f"Average Waiting Time: {avg_waiting_time:.2f}")


# Example Input
processes = ["P1", "P2", "P3", "P4"]
arrival_times = [0, 2, 4, 5]
burst_times = [7, 4, 1, 4]

# Run the SJF Scheduling Algorithm
sjf_scheduling(processes, arrival_times, burst_times)
