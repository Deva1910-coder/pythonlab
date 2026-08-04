size = 5
queue = [None] * size
front = -1
rear = -1

def enqueue():
    global front, rear
    if rear == size - 1:
        print("Queue is full")
    else:
        car = input("Enter car no.: ")
        if front == -1:
            front = 0
        rear += 1
        queue[rear] = car
        print(car, "Entered the parking")

def dequeue():
    global front, rear
    if front == -1 or front > rear:
        print("Queue is empty")
    else:
        print(queue[front] + " left the parking")
        front += 1
        if front > rear:
            front = rear = -1

def display():
    if front == -1 or front > rear:
        print("Queue is empty")
    else:
        print("Cars in the parking queue:")
        for i in range(front, rear + 1):
            print(queue[i])

while True:
    print("\n1.Enqueue\n2.Dequeue\n3.Display\n4.Exit")
    try:
        choice = int(input("Enter the choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        print("Exiting program.")
        break
    else:
        print("Invalid ")
