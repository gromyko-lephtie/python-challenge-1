def solution(A):
    
    def digit_sum(num):
        return sum(int(digit) for digit in str(num))

    
    sums_dict = {}

    
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            sum_of_digits = digit_sum(A[i]) + digit_sum(A[j])
            
            if sum_of_digits not in sums_dict:
                sums_dict[sum_of_digits] = []
            sums_dict[sum_of_digits].append((A[i], A[j]))

    max_sum = -1

   
    for sum_val, pairs in sums_dict.items():
        if len(pairs) > 1:
        
            max_sum = max(max_sum, max([pair[0] + pair[1] for pair in pairs]))

    return max_sum


print(solution([51, 71, 17, 42]))  
print(solution([42, 33, 60]))      
print(solution([51, 32, 43]))      
