def solution(A):
    N = len(A)
    moves = 0
    
    for i in range(1, N):  
        diff = A[i] - 10  
        if diff > 0:  
            A[i] -= diff  
            A[i - 1] += diff  
            moves += diff  
        
    for i in range(N - 2, -1, -1):  
        diff = A[i] - 10  
        if diff > 0:  
            A[i] -= diff  
            A[i + 1] += diff  
            moves += diff  
        
    
    if all(brick_count == 10 for brick_count in A):
        return moves  
    else:
        return -1  


print(solution([7, 15, 10, 8]))  
print(solution([11, 10, 8, 12, 8, 10, 11]))  
print(solution([7, 14, 10]))  
