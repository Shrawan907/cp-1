def sum_arr(list1):
    sum1=0
    for i in list1:
        sum1=sum1+i
    print(sum1)
n=int(input())
list1=list(map(int,input().split()))
sum_arr(list1)