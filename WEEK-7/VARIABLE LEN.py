def total_marks(*marks):
    """Return the total and average of any number of subject marks."""
    total = sum(marks)
    average = total / len(marks)
    return total, average


# Test with 3 marks
total, average = total_marks(80, 75, 90)
print("For 3 marks:")
print("Total:", total)
print("Average:", average)

print()

# Test with 5 marks
total, average = total_marks(80, 75, 90, 85, 70)
print("For 5 marks:")
print("Total:", total)
print("Average:", average)

print()

# Test with 1 mark
total, average = total_marks(95)
print("For 1 mark:")
print("Total:", total)
print("Average:", average)