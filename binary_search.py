list = [10,20,30,40,50,60,70,80,90,100]
searchNum = int(input("Enter number to search : "))
start = 0
end = len(list)-1
flag=False
while start <= end and flag==False:
    midpoint = (start+end)//2
    if searchNum == list[midpoint]:
        print(f'Number is found at index {midpoint}')
        flag=True
    else:
        if list[midpoint] <= searchNum:
            start= midpoint+1
        if list[midpoint] >= searchNum:
            end= midpoint-1
if flag==False:
    print('Number not found')
