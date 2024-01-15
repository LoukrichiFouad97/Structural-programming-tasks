def printArray(arr, size):
    for i in range(size):
        print(arr[i], end=" ")
        if (i + 1) % 10 == 0:
            print()  # Print a new line after every 10 elements
    print()  # Print a final new line if needed

def main():
    size = int(input("Enter the size of the array: "))
    
    # Input elements for the array
    arr = [float(input(f"Enter element {i + 1}: ")) for i in range(size)]

    # Display the array using the printArray function
    print("Array Contents:")
    printArray(arr, size)

if __name__ == "__main__":
    main()
