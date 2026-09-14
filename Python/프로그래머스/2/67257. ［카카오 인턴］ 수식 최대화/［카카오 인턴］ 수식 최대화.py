from itertools import permutations

def caculation(exp,op):
    nums = []
    ops = []
    num = ""
    for x in exp:
        if x=="*" or x =="+" or x=="-":
            nums.append(int(num))
            num=""
            ops.append(x)
        else:
            num+=x
    nums.append(int(num))

    for o in op:
        i = 0
        while i < len(ops):
            if ops[i] == o:
                if o=="*":
                    result = nums[i] * nums[i+1]
                elif o=="-":
                    result = nums[i] - nums[i+1]
                elif o=="+":
                    result = nums[i] + nums[i+1]
                
                nums[i] = result
                nums.pop(i+1)
                ops.pop(i)
            else:
                i+=1
    
    return abs(nums[0])
    
        

def solution(expression):
    answer = [0]
    op = ["*","+","-"]
    per = list(permutations(op,3))
    
    for pe in per:
        answer.append(caculation(expression,pe))
                
            
    return max(answer)