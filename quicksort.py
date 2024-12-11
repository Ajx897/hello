def quick_sort(arr):
    if len(arr) <= 1: 
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)



def main():
    n = int(input("Enter the number of students: "))
    percentages = []
    print("Enter the percentages of students:")
    for i in range(n):
        percentages.append(float(input(f"Student {i+1}: ")))
    sorted_percentages = quick_sort(percentages)
    print("\nSorted Percentages in Ascending Order:")
    print(sorted_percentages)
    print("\nTop Five Scores:")
    print(sorted_percentages[-5:][::-1])
if __name__ == "__main__":
    main()
