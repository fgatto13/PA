def min_delay(jobs):
    """
    Minimize delay for a list of jobs based on their due dates.
    
    Args:
    jobs (list of tuples): Each tuple contains (t_j, d_j) where:
        t_j = processing time of job j
        d_j = due date of job j
    
    Returns:
    list of tuples: Each tuple contains (s, f) where:
        s = start time of job
        f = finish time of job
    """
    # Step 1: Sort jobs by their due date d_j
    jobs_sorted = sorted(jobs, key=lambda job: job[1])
    
    # Step 2: Initialize the starting time and the schedule list
    t = 0
    S = []
    L = 0
    
    # Step 3: Schedule each job based on sorted due dates
    for t_j, d_j in jobs_sorted:
        s = t               # Start time of the current job
        f = t + t_j         # Finish time of the current job
        l = max(0, f - d_j) # this is used to calulate the delay
        L += l              # here we add the delay for the job j to L
        S.append((s, f))    # Add the interval to the schedule
        t = f               # Update current time to the finish time of the current job
    
    return S, L

# Example usage with sample data
jobs = []
risp = 0

# Improved input handling loop
while True:
    try:
        t = int(input("Insert time units (t_j): "))
        d = int(input("Insert due time (d_j): "))
        jobs.append((t, d))
        
        risp = input("Another? (Y for Yes, N for No): ").strip().lower()
        if risp == 'n':
            break
    except ValueError:
        print("Invalid input, please enter valid integers for time units and due time.")

S, L = min_delay(jobs)

# Display the schedule
print("Schedule intervals (s, f) based on job start and finish times:")
for idx, (s, f) in enumerate(S):
    print(f"Job {idx + 1}: Start at {s}, Finish at {f}")
print(L)
