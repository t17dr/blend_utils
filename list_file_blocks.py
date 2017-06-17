import sys, os

def read_header(file):
    identifier = file.read(7).decode("utf-8")
    print("Identifier: " + identifier)
    pointer_size = file.read(1).decode("utf-8")
    print("32 bit pointers") if pointer_size == '_' else print("64 bit pointers")
    endianness = file.read(1).decode("utf-8")
    print("Little endian") if endianness == 'v' else print("Big endian")
    version = file.read(3).decode("utf-8")
    print("Version number: " + version)

    return (4 if pointer_size == '_' else 8, "little" if endianness == 'v' else "big")

def read_file_block(file, pointer_size, endianness):
    pos = format(file.tell(), '0x')
    print("File position: " + pos)
    code = file.read(4).decode("utf-8")
    if code == "":
        return False
    print("Block code: " + code)
    size = int.from_bytes(file.read(4), byteorder=endianness)
    if size == 0:
        return False
    print("Block size: " + str(size))
    memory_addr = int.from_bytes(file.read(pointer_size), byteorder=endianness)
    memory_addr_hex = format(memory_addr, '0x')
    print("Old memory address: " + memory_addr_hex)
    sdna_index = int.from_bytes(file.read(4), byteorder=endianness)
    print("SDNA index: " + str(sdna_index))
    count = int.from_bytes(file.read(4), byteorder=endianness)
    print("Number of structures: " + str(count))
    file.seek(size, 1)

    print("")
    return True

def main():
    with open(sys.argv[1], 'rb') as file:
        print("==== HEADER ====\n")
        pointer_size, endianness = read_header(file)
        print("\n==== FILE BLOCKS ====\n")
        while not file.tell() == os.fstat(file.fileno()).st_size:
            ok = read_file_block(file, pointer_size, endianness)
            if not ok:
                # End of file?
                break
if __name__ == "__main__":
    main()
