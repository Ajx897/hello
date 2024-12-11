def calculate_average(scores):
    valid_scores = [score for score in scores if score != -1]
    if valid_scores:
        return sum(valid_scores) / len(valid_scores)
    else:
        return 0

def find_highest_and_lowest(scores):
    valid_scores = [score for score in scores if score != -1]
    if valid_scores:
        return max(valid_scores), min(valid_scores)
    else:
        return None, None

def count_absent_students(scores):
    return scores.count(-1)

def find_highest_frequency(scores):
    valid_scores = [score for score in scores if score != -1]
    if valid_scores:
        frequency = {}
        for score in valid_scores:
            frequency[score] = frequency.get(score, 0) + 1
        max_freq = max(frequency.values())
        return [score for score, freq in frequency.items() if freq == max_freq]
    else:
        return []

def main():
    # Input marks for N students
    N = int(input("Enter the number of students: "))
    print("Enter the marks scored by the students (-1 for absent): ")
    scores = [int(input(f"Student {i+1}: ")) for i in range(N)]
    
    # Compute and display results
    average = calculate_average(scores)
    highest, lowest = find_highest_and_lowest(scores)
    absent_count = count_absent_students(scores)
    most_frequent = find_highest_frequency(scores)
    
    print("\n--- Results ---")
    print(f"Average score of the class: {average:.2f}" if average > 0 else "No scores available to calculate average.")
    print(f"Highest score: {highest}" if highest is not None else "No valid scores.")
    print(f"Lowest score: {lowest}" if lowest is not None else "No valid scores.")
    print(f"Number of students absent for the test: {absent_count}")
    print(f"Mark(s) with the highest frequency: {', '.join(map(str, most_frequent))}" if most_frequent else "No scores available to analyze frequency.")

if __name__ == "__main__":
    main()
