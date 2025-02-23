try:
    file = open("testfile.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("Error: File not found.")
finally:
    print("Closing file...")
    if 'file' in locals() and not file.closed:
        file.close()