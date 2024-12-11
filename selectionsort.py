def selection_sort(arr):
    """Sorts an array of floating-point numbers in ascending order using Selection Sort."""
    n = len(arr)
    for i in range(n):
        # Find the index of the minimum element in the unsorted part of the array
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]

def main():
    # Input: Number of students and their percentages
    n = int(input("Enter the number of students: "))
    percentages = []
    print("Enter the percentages of students:")
    for i in range(n):
        percentages.append(float(input(f"Student {i+1}: ")))

    # Sort the array using Selection Sort
    print("\nOriginal Percentages:")
    print(percentages)

    selection_sort(percentages)

    # Display the sorted array
    print("\nSorted Percentages in Ascending Order:")
    print(percentages)

if __name__ == "__main__":
    main()
