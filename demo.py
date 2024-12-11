def bubble(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
def main():
    n=int(input('Enter no of student:'))
    percentages=[]
    for i in range(n):
        percentages.append(float(input(f'student {i+1}:')))

    print('original percentage:',percentages)

    bubble(percentages)
    print('After Sorting:',percentages)
    print('Top five scores:',percentages[-5:6])

if __name__=="__main__":
    main()
