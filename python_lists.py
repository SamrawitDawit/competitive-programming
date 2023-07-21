if __name__ == '__main__':
    N = int(input())
    myList = []
    for i in range(N):
        command = input().split(" ")
        if command[0] == "insert":
            i, e = int(command[1]), int(command[2])
            myList.insert(i,e)
        elif command[0] == "print":
            print(myList)
        elif command[0] == "remove":
            e = int(command[1])
            myList.remove(e)
        elif command[0] == "append":
            e = int(command[1])
            myList.append(e)
        elif command[0] == "sort":
            myList.sort()
        elif command[0] == "pop":
            if myList:
                myList.pop()
        elif command[0] == "reverse":
            myList.reverse()
