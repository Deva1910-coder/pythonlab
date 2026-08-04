class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self):
        car = input("Enter car no.: ")
        new_node = Node(car)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(car, "entered the parking")

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
        else:
            print(self.front.data + " left the parking")
            self.front = self.front.next
            if self.front is None:
                self.rear = None

    def display(self):
        if self.front is None:
            print("Queue is empty")
        else:
            print("Cars in the parking queue:")
            temp = self.front
            while temp is not None:
                print(temp.data, end=" -> ")
                temp = temp.next
            print("None")

parking = Queue()

while True:
    print("\n1.Enqueue\n2.Dequeue\n3.Display\n4.Exit")
    choice = int(input("Enter the choice: "))

    if choice == 1:
        parking.enqueue()
    elif choice == 2:
        parking.dequeue()
    elif choice == 3:
        parking.display()
    elif choice == 4:
        print("Exiting program.")
        break
    else:
        print("Invalid")
