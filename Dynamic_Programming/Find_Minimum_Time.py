# Find Minimum Time to Finish All Jobs: https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/

"""
The time complexity is O(nlog(sum(jobs)−max(jobs))), where n is the number of jobs. This is because we perform a binary search in the range of [max(jobs), sum(jobs)] and for each mid value, we perform a depth-first search to check if it's possible to divide the jobs among the workers.

The space complexity is O(n), because in the worst-case scenario, the depth of the recursion tree can go up to n.
"""

def minimumTimeRequired(jobs, k):
    def check(limit):
        "Check if it's possible to divide jobs s.t. each worker's workload is <= limit"
        workloads = [0] * k
        return dfs(0, limit, workloads)

    def dfs(i, limit, workloads):
        if i >= len(jobs):
            return True
        for j in range(k):
            if workloads[j] + jobs[i] <= limit:
                workloads[j] += jobs[i]
                if dfs(i+1, limit, workloads):
                    return True
                workloads[j] -= jobs[i]
            if workloads[j] == 0:
                break
        return False

    jobs.sort(reverse=True)
    l, r = jobs[0], sum(jobs)
    while l < r:
        mid = (l + r) // 2
        if check(mid):
            r = mid
        else:
            l = mid + 1
    return l

print(minimumTimeRequired([3,2,3], 3))  # Expected output: 3
print(minimumTimeRequired([1,2,4,7,8], 2))  # Expected output: 11
