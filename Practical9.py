def priority_scheduling(processes, arrival_times, burst_times, priorities):
    n = len(processes)  # Number of processes
    completed = [False] * n  # To track completed processes
    completion_times = [0] * n  # Completion time for each process
    turnaround_times = [0] * n  # Turnaround time for each process
    waiting_times = [0] * n  # Waiting time for each process

    current_time = 0
    completed_count = 0

    while completed_count < n:
        highest_priority_index = -1
        for i in range(n):
            if arrival_times[i] <= current_time and not completed[i]:
                if (
                    highest_priority_index == -1
                    or priorities[i] < priorities[highest_priority_index]
                ):
                    highest_priority_index = i

        if highest_priority_index == -1:
            current_time += 1  # No process available; increase time
            continue

        # Process the selected process
        current_time += burst_times[highest_priority_index]
        completion_times[highest_priority_index] = current_time
        turnaround_times[highest_priority_index] = (
            completion_times[highest_priority_index]
            - arrival_times[highest_priority_index]
        )
        waiting_times[highest_priority_index] = (
            turnaround_times[highest_priority_index]
            - burst_times[highest_priority_index]
        )

        completed[highest_priority_index] = True
        completed_count += 1

    # Print results
    print("Process\tArrival\tBurst\tPriority\tCompletion\tTurnaround\tWaiting")
    for i in range(n):
        print(
            f"{processes[i]}\t{arrival_times[i]}\t{burst_times[i]}\t{priorities[i]}\t\t{completion_times[i]}\t\t{turnaround_times[i]}\t\t{waiting_times[i]}"
        )

    avg_turnaround_time = sum(turnaround_times) / n
    avg_waiting_time = sum(waiting_times) / n
    print(f"\nAverage Turnaround Time: {avg_turnaround_time:.2f}")
    print(f"Average Waiting Time: {avg_waiting_time:.2f}")


# Example Input
processes = ["P1", "P2", "P3", "P4"]
arrival_times = [0, 1, 2, 3]
burst_times = [5, 3, 8, 6]
priorities = [2, 1, 3, 4]
priority_scheduling(processes, arrival_times, burst_times, priorities)
