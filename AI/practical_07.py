# Write a program to solve tower of Hanoi problem

def toh(disks, source, auxiliary, target):
    if(disks==1):
        print("Move disk 1 from rod " + str(source) + " to rod " + str(target))
        return
    toh(disks-1, source, target, auxiliary)
    print("Move disk " + str(disks) + " from rod " + str(source) + " to rod " + str(target))
    toh(disks-1, auxiliary, source, target)
disks = int(input("Enter number of disks: "))
toh(disks, 'A', 'B', 'C')
