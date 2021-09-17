def solution(word):
    counts = [781, 156, 31, 6, 1]
    letters = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    answer = 0
    for i in range(len(word)):
        answer += counts[i] * letters[word[i]]
        answer += 1
    return answer

print(solution("I"))
