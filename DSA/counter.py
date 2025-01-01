from collections import Counter

def min_deletions_to_unique_counts(A):
    freq = Counter(A)  # Get frequency of each element
    freq_count = Counter(freq.values())  # Get frequency of the frequencies
    deletions = 0
    
    # Process each frequency count to ensure all frequencies are unique
    for count in sorted(freq_count.keys(), reverse=True):
        while freq_count[count] > 1:  # While there are duplicate frequencies
            deletions += 1
            freq_count[count] -= 1  # Reduce current frequency count by 1
            if count > 1:
                freq_count[count - 1] += 1  # Move one occurrence to the next lower frequency
    
    return deletions

# Example usage:
A = [1, 1, 1, 2, 2, 2]
print(min_deletions_to_unique_counts(A))  # Output should be 1
