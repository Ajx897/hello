def bubble_sort(arr):
    """Sorts an array of floating-point numbers in ascending order using Bubble Sort."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):  # Last i elements are already sorted
            if arr[j] > arr[j+1]:
                # Swap if the current element is greater than the next
                arr[j], arr[j+1] = arr[j+1], arr[j]

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

    # Sort the array using Bubble Sort
    bubble_sort(percentages)

    # Display the sorted array
    print("\nSorted Percentages in Ascending Order:")
    print(percentages)

    # Display the top five scores
    print("\nTop Five Scores:")
    print(percentages[-5:][::-1])  # Take the last 5 elements and reverse for descending order

if __name__ == "__main__":
    main()