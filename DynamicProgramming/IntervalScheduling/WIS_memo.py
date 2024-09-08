def find_p_values(jobs):
    # Sort jobs by finish time
    jobs.sort(key=lambda x: x[1])  # jobs is a list of tuples (s, f, w)

    n = len(jobs)
    p = [-1] * n  # Initialize p array with -1
    
    # To find p[j], we need to find the maximum index i < j such that job i is compatible with job j
    for j in range(n):
        s_j, f_j, w_j = jobs[j]
        max_index = -1

        # Iterate over jobs before j to find the maximum compatible index
        for i in range(j):
            s_i, f_i, w_i = jobs[i]
            if f_i <= s_j:
                max_index = i
        
        p[j] = max_index
    
    return p

def M_Compute_opt(M, j, jobs, p):
    # Base case
    if j == -1:
        return 0
    if M[j] == -1:  # Memoization: only compute if not already done
        M[j] = max(jobs[j][2] + M_Compute_opt(M, p[j], jobs, p), 
                   M_Compute_opt(M, j-1, jobs, p))
    return M[j]

def find_solution(M, j, jobs, p):
    if j == -1:
        return
    elif jobs[j][2] + M[p[j]] > M[j-1]:
        find_solution(M, p[j], jobs, p)
        print(f"Job {j} -> {jobs[j]}")
    else:
        find_solution(M, j-1, jobs, p)

# Example usage:
jobs = [(1, 3, 2), (2, 5, 4), (4, 6, 1), (5, 7, 3)]

p_values = find_p_values(jobs)
M = [-1] * len(jobs)  # Initialize memoization array M with -1

# Compute optimal weight schedule
optimal_value = M_Compute_opt(M, len(jobs)-1, jobs, p_values)
print(f"Optimal value: {optimal_value}")

# Reconstruct the solution
print("Selected jobs:")
find_solution(M, len(jobs)-1, jobs, p_values)
