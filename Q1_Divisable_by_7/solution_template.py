from time import time
import json
def solution(start, end, divisable_by=7) -> list[str]:
    results = []
    ## solution here
    return results

if __name__ == "__main__":
    with open("answer.json", "r") as f:
        correct_answer = json.load(f)
    start_time = time()
    answer = solution(2000, 3200)
    spent_time = (time()-start_time)/1000
    if correct_answer == answer:
        is_correct = True
        msg = "correct"
    else:
        is_correct = False
        msg = f"incorrect. Expecting {correct_answer}, given {answer}"
    print(f"spent time: {spent_time} sec")    
    print("answer is", msg)


