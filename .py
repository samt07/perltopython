import sys

def process_data():
    # Fast I/O similar to reading/writing in C++
    input = sys.stdin.read
    data = input().strip().split()
    
    results = []
    for value in data:
        # Example processing
        result = int(value) ** 3  # Cubing the value (assuming int overflow not an issue in Python)
        results.append(str(result))
    
    print(" ".join(results))

if __name__ == "__main__":
    process_data()

