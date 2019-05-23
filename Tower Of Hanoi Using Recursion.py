def Tower_of_Hanoi(height, from_pole, to_pole, with_pole):
    if height >= 1:
        Tower_of_Hanoi(height-1,from_pole, with_pole, to_pole)
        print("Move Disk {} from Pole {} to Pole {}".format(height,from_pole,to_pole))
        Tower_of_Hanoi(height-1, with_pole, to_pole, from_pole)

n=int(input("Enter the no of Disks : "))
Tower_of_Hanoi(n,"A","C","B")