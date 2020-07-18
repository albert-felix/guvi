n, mark = input().split(" ")
marks = [int(x) for x in input().split(" ")]
for i in range(len(marks)):
    if marks[i] == int(mark):
        print(i)
        break
else:
    print(-1)
