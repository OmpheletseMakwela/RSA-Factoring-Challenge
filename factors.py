import sys

def factorize(number):
    factors = []
    for i in range(2, int(number ** 0.5) + 1):
        while number % i == 0:
            factors.append(i)
            number //= i
    if number > 1:
        factors.append(number)
    return factors

def main(file_path):
    with open(file_path, 'r') as file:
        numbers = file.readlines()

    for num in numbers:
        num = int(num.strip())
        factors = factorize(num)
        print(f"{num}={'*'.join(map(str, factors[:2]))}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    input_file = sys.argv[1]
    main(input_file)
