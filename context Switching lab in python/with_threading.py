import threading
import time

process_1_operation = [
    ("ADD", 5, 3),
    ("SUB", 10, 4),
]

process_2_operation = [
    ("MUL", 5, 3),
    ("DIV", 10, 4),
    ("MOD", 9, 4),
]


def execute_operation(operation, *args):
    if operation == "ADD":
        result = args[0] + args[1]
        print(f"AddResult: {result}")
    elif operation == "SUB":
        result = args[0] - args[1]
        print(f"SubResult: {result}")
    elif operation == "MUL":
        result = args[0] * args[1]
        print(f"MulResult: {result}")
    elif operation == "DIV":
        if args[1] != 0:
            result = args[0] / args[1]
            print(f"DivResult: {result}")
        else:
            print("Error: Division by zero is not allowed.")
    elif operation == "MOD":
        result = args[0] % args[1]
        print(f"ModResult: {result}")


def process_operations(operations, process_id):
    for operation in operations:
        op_name, arg1, arg2 = operation
        print(f"Process {process_id}: Performing {op_name} with arguments {arg1} and {arg2}")
        execute_operation(op_name, arg1, arg2)
        time.sleep(1)


thread1 = threading.Thread(target=process_operations, args=(process_1_operation, "1"))
thread2 = threading.Thread(target=process_operations, args=(process_2_operation, "2"))


thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("All operations completed.")
