stack = []
max_capacity = 100

def push(name):
    if len(stack) >= max_capacity:
        print("Stack overflow")
    else:
        stack.append(name)
        print(f"Added: '{name}'")

def pop():
    if len(stack) == 0:
        print("Cannot pop! The stack is empty.")
        return None
    
    removed_book = stack.pop()
    print(f"Removed: '{removed_book}'")
    return removed_book

def peek():
    if len(stack) == 0:
        print("The stack is empty.")
        return None
    
    top_book = stack[-1]
    print(f"Top book is: '{top_book}'")
    return top_book

def display():
    if len(stack) == 0:
        print("The stack is empty.")
        return
    
    print("\n--- Book Pile (Top to Bottom) ---")
    for book in reversed(stack):
        print(book)

while True:
    print("\n--- BOOK STACK MENU ---")
    print("1. Push (Add a book)")
    print("2. Pop (Remove top book)")
    print("3. Peek (View top book)")
    print("4. Display Stack")
    print("5. Exit")
    
    choice = input("\nEnter your choice (1-5): ").strip()

    if choice == "1":
        title = input("Enter the book title: ").strip()
        if title:
            push(title)
        else:
            print("\nError: Book title cannot be empty.")
            
    elif choice == "2":
        pop()
        
    elif choice == "3":
        peek()
        
    elif choice == "4":
        display()
        
    elif choice == "5":
        print("\nExiting")
        break
        
    else:
        print("\nInvalid choice")
