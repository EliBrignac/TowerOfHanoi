

pole1 = []
pole2 = []
pole3 = []

def print_towers():
    print("Pole1 =",pole1)
    print("Pole2 =",pole2)
    print("Pole3 =",pole3)
    print('\n')
    return

def TowerOfHanoi(n, pole1, pole2, pole3):
    if n==1:
        pole2.append(pole1[-1])
        pole1.pop()
        print_towers()
        return
    TowerOfHanoi(n - 1, pole1, pole3, pole2)
    pole2.append(pole1[-1])
    pole1.pop()
    print_towers()
    TowerOfHanoi(n - 1, pole3, pole2, pole1)
    return

def setup(n):
    for i in range(0,n):
        pole1.append(n - i)
    return

#n is the amount of disks in the game
n = 10
setup(n)
print_towers()
TowerOfHanoi(n, pole1, pole3, pole2)


