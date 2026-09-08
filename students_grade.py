students = {
    "Alice": [85, 90, 78],
    "Bob": [70, 88, 92],
    "Charlie": [95, 85, 87],
    "Diana": [60, 72, 68]
}

def calculate_average(marks):
    return sum(marks) / len(marks)

def display_results():
    print("Student | Average Grade")
    print("-"*25)
    for name, marks in students.items():
        avg = calculate_average(marks)
        print(f"{name:7} | {avg:.2f}")

if __name__ == "__main__":
    display_results()
