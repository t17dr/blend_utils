import sys

def main():
    repaired_end = int(sys.argv[3])
    new_start = int(sys.argv[4])
    with open(sys.argv[1], 'rb') as repaired, open(sys.argv[2], 'rb') as new, open(sys.argv[1] + ".repaired", 'wb') as result:
        repaired_data = repaired.read(repaired_end)
        new.seek(new_start)
        new_data = new.read()
        result.write(repaired_data)
        result.write(new_data)

if __name__ == "__main__":
    main()
