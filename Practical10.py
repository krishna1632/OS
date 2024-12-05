def srjf_scheduling(processes, arrival_times, burst_times):
    n = len(processes)  # Number of processes
    remaining_times = burst_times[:]  # Remaining burst times for each process
    completion_times = [0] * n  # Completion times
    turnaround_times = [0] * n  # Turnaround times
    waiting_times = [0] * n  # Waiting times

    current_time = 0
    completed_count = 0
    shortest_job_index = -1

    while completed_count < n:
        # Find process with shortest remaining time
        shortest_job_index = -1
        for i in range(n):
            if arrival_times[i] <= current_time and remaining_times[i] > 0:
                if (
                    shortest_job_index == -1
                    or remaining_times[i] < remaining_times[shortest_job_index]
                ):
                    shortest_job_index = i

        if shortest_job_index == -1:
            current_time += 1  # No process available; increase time
            continue

        # Process the selected process
        remaining_times[shortest_job_index] -= 1
        current_time += 1

        if remaining_times[shortest_job_index] == 0:
            completion_times[shortest_job_index] = current_time
            turnaround_times[shortest_job_index] = (
                completion_times[shortest_job_index] - arrival_times[shortest_job_index]
            )
            waiting_times[shortest_job_index] = (
                turnaround_times[shortest_job_index] - burst_times[shortest_job_index]
            )
            completed_count += 1

    # Print results
    print("Process\tArrival\tBurst\tCompletion\tTurnaround\tWaiting")
    for i in range(n):
        print(
            f"{processes[i]}\t{arrival_times[i]}\t{burst_times[i]}\t{completion_times[i]}\t\t{turnaround_times[i]}\t\t{waiting_times[i]}"
        )

    avg_turnaround_time = sum(turnaround_times) / n
    avg_waiting_time = sum(waiting_times) / n
    print(f"\nAverage Turnaround Time: {avg_turnaround_time:.2f}")
    print(f"Average Waiting Time: {avg_waiting_time:.2f}")


# Example Input
processes = ["P1", "P2", "P3", "P4"]
arrival_times = [0, 1, 2, 3]
burst_times = [8, 4, 2, 1]
srjf_scheduling(processes, arrival_times, burst_times)
