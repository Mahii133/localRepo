import ctypes

class MeraList:
    def __init__(self):
        self.size = 1   # Initial size of the array
        self.n = 0      # Number of items currently in the array
        self.A = self.__make_array(self.size)  # Create C type array with initial size
        
    def __len__(self):
        return self.n
    
    def __str__(self):
        result = ''
        for i in range(self.n):
            result += str(self.A[i]) + ','
        return '[' + result[:-1] + ']'
    
    def __getitem__(self,index):
        if 0 <= index < self.n:
            return self.A[index]
        else:
            return 'IndexError - Index out of range'
        
    def __delitem__(self, pos):
        if pos < 0 or pos >= self.n:
            return 'IndexError - Index out of range'

        for i in range(pos, self.n - 1):
            self.A[i] = self.A[i + 1]
        
        self.n -= 1
    
    def append(self, item):
        if self.n == self.size:
            # Resize the array if it's full
            self.__resize(self.size * 2)

        self.A[self.n] = item
        self.n += 1

    def pop(self):
        if self.n == 0:
            return 'Empty list'
        popped_item = self.A[self.n - 1]
        self.n -= 1
        return popped_item

    def interactive_pop(self):
        if self.n == 0:
            return 'Empty list'
        print("Popped item:", self.A[self.n - 1])
        self.n -= 1

    def clear(self):
        self.n = 0
        self.size = 1
        self.A = self.__make_array(self.size)  # Reinitialize the array

    def find(self,item):
        for i in range(self.n):
            if self.A[i]== item:
                return i 
            
        return 'ValueError - not in list'
    
    def insert(self,pos,item):

        if self.n == self.size:
            self.__resize(self.size*2)

        for i in range(self.n, pos, -1):
            self.A[i] = self.A[i-1]
        self.A[pos] = item
        self.n = self.n + 1

    def remove(self,item):
        pos = self.find(item)

        if type(pos) == int:
            self.__delitem__(pos)
        else:
            return pos

    def __resize(self, new_capacity):
        # Create a new array with the new capacity
        B = self.__make_array(new_capacity)
        self.size = new_capacity
        
        # Copy the contents of A to B
        for i in range(self.n):
            B[i] = self.A[i]

        # Reassign A to the new resized array
        self.A = B
    
    def __make_array(self, capacity):
        # Create a C type array (Static and referential) with size capacity
        return (capacity * ctypes.py_object)()

# Example usage with user input:
L = MeraList()

while True:
    user_input = input("Enter an item to append (or 'done' to finish): ")
    if user_input.lower() == 'done':
        break
    L.append(user_input)

print("Final List:", L)
print("Length of the array:", len(L))

# User wants to access an index of the list
index_to_access = int(input("Enter the index to access: "))
print("Item at index", index_to_access, ":", L[index_to_access])

# User wants to pop items
while True:
    pop_choice = input("Would you like to pop the last item? (yes/no): ")
    if pop_choice.lower() == 'yes':
        if len(L) == 0:
            print("List is empty.")
            break
        L.interactive_pop()
        print("Updated List:", L)
        print("Length of the array:", len(L))
    elif pop_choice.lower() == 'no':
        print("No more items will be popped.")
        break
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")

# User wants to clear the entire list
clear_choice = input("Would you like to clear the entire list? (yes/no): ")
if clear_choice.lower() == 'yes':
    L.clear()
    print("List has been cleared.")
    print("Updated List:", L)
    print("Length of the array:", len(L))
else:
    print("List was not cleared.")

# User wants to find an item's index
find_item = input("Enter an item to find its index: ")
print("Index of", find_item, ":", L.find(find_item))

# User wants to insert an item at a specific position
insert_pos = int(input("Enter the position to insert the item: "))
insert_item = input("Enter the item to insert: ")
L.insert(insert_pos, insert_item)
print("Item", insert_item, "inserted at position", insert_pos)
print("Updated List:", L)
print("Length of the array:", len(L))

# User wants to delete an item at a specific position
delete_pos = int(input("Enter the position to delete the item: "))
del L[delete_pos]
print("Item at position", delete_pos, "deleted.")
print("Updated List:", L)
print("Length of the array:", len(L))

# User wants to remove an item from the list
remove_item = input("Enter an item to remove: ")
result = L.remove(remove_item)
if result is not None:
    print(result)
else:
    print("Item", remove_item, "removed from the list.")
    print("Updated List:", L)
    print("Length of the array:", len(L))
