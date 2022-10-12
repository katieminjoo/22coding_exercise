
def solution(food_times, k):
    answer = 0
    count = 0
    while True:
        for idx in range(len(food_times)):
            if food_times[idx] > 0 :
                food_times[idx] -= 1
                count += 1
                print(food_times, count)
        if count == k :
            answer = food_times[idx] +1
            break
    
    return answer

print(solution([3,1,2],5))