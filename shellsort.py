def shell_sort(arr):
    """Sorts an array of floating-point numbers in ascending order using Shell Sort."""
    n = len(arr)
    gap = n // 2  # Start with a large gap and reduce it

    # Start with a large gap and reduce it after each pass
    while gap > 0:
        # Perform insertion sort for this gap size
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # Compare and move elements with the given gap
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2  # Reduce the gap

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

    # Sort the array using Shell Sort
    shell_sort(percentages)

    # Display the sorted array
    print("\nSorted Percentages in Ascending Order:")
    print(percentages)

    # Display top five scores (if available)
    print("\nTop 5 Scores:")
    top_scores = percentages[-5:]  # Get the top 5 scores (last 5 elements after sorting)
    print(top_scores)

if __name__ == "__main__":
    main()
