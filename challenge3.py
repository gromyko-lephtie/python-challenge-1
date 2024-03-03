def solution(N):
    # Generate a string containing all lowercase letters
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if N <= 26:
        return alphabet[:N]


    repeated_alphabet = alphabet * (N // 26) + alphabet[:N % 26]

    return repeated_alphabet


print(solution(3))   
print(solution(5))   
print(solution(30))  
