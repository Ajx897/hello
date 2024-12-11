def insertion_sort(arr):
    """Sorts an array of floating-point numbers in ascending order using Insertion Sort."""
    n = len(arr)
    for i in range(1, n):  # Start from the second element
        key = arr[i]  # The current element to be inserted
        j = i - 1  # The last index of the sorted portion of the array

        # Move elements of arr[0..i-1] that are greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift elements to the right
            j -= 1
        
        # Place the key in its correct position
        arr[j + 1] = key

def main():
    # Input: Number of students and their percentages
    n = int(input("Enter the number of students: "))
    percentages = []
    print("Enter the percentages of students:")
    for i in range(n):
        percentages.append(float(input(f"Student {i+1}: ")))

    # Display the original percentages
    print("\nOriginal Percentages:")
    print(percentages)

    # Sort the array using Insertion Sort
    insertion_sort(percentages)

    # Display the sorted array
    print("\nSorted Percentages in Ascending Order:")
    print(percentages)

if __name__ == "__main__":
    main()
