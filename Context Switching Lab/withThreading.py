import threading
import time

file_list = ["with/File1.txt", "with/File2.txt", "with/File3.txt", "with/File4.txt", "with/File5.txt"]

file_contents = {
    "with/File1.txt": [("ADD", 10, 5, "AddResult"), ("SUB", 30, 4, "SubResult")],
    "with/File2.txt": [
        ("MUL", 3, 6, "MulResult"),
        ("DIV", 10, 2, "DivResult"),
        ("MOD", 15, 5, "ModResult"),
    ],
    "with/File3.txt": [
        ("DIV", 10, 2, "DivResult"),
        ("MOD", 15, 5, "ModResult"),
        ("MUL", 34, 4, "MulResult"),
    ],
    "with/File4.txt": [
        ("ADD", 44, 6, "AddResult"),
        ("SUB", 30, 4, "SubResult"),
        ("MUL", 34, 4, "MulResult"),
        ("DIV", 34, 8, "DivResult"),
    ],
    "with/File5.txt": [
        ("ADD", 44, 6, "AddResult"),
        ("SUB", 30, 4, "SubResult"),
    ]
}


for file_path in file_list:
    with open(file_path, "w") as f:
        lines = file_contents.get(file_path, [])
        for operation, op1, op2, result in lines:
            f.write(f"{operation} {op1} {op2} {result}\n")
        print(f"File {file_path} created")


def execute_operation(operation, *args):
    if operation == "ADD":
        result = int(args[0]) + int(args[1])
        print(f"AddResult: {result}")
    elif operation == "SUB":
        result = int(args[0]) - int(args[1])
        print(f"SubResult: {result}")
    elif operation == "MUL":
        result = int(args[0]) * int(args[1])
        print(f"MullResult: {result}")
    elif operation == "DIV":
        if args[1] != 0:
            result = int(args[0]) / int(args[1])
            print(f"DivResult: {result}")
        else:
            print("Error: Division by zero")
    elif operation == "MOD":
        result = int(args[0]) % int(args[1])
        print(f"ModResult: {result}")


def process_from_file(fileName, process_id):

    with open(fileName, "r") as f:
        tasks = f.readlines()

    for line in tasks:
        line = line.strip()
        if line.startswith(f"Process {process_id}"):
            continue

        if line.startswith("process"):
            break

        operation_parts = line.split()
        operation = operation_parts[0]
        args = operation_parts[1:3]
        execute_operation(operation, *args)
        time.sleep(1)


thread1 = threading.Thread(target=process_from_file, args=(file_list[0], "1"))
thread2 = threading.Thread(target=process_from_file, args=(file_list[1], "1"))
thread3 = threading.Thread(target=process_from_file, args=(file_list[2], "1"))
thread4 = threading.Thread(target=process_from_file, args=(file_list[3], "1"))
thread5 = threading.Thread(target=process_from_file, args=(file_list[4], "1"))

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()


thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()