import threading
import time

process_1_operation = [
    ("ADD", 5, 3),
    ("SUB", 10, 4),
    ("ADD", 15, 4)
]

process_2_operation = [
    ("MUL", 7, 6),
    ("DIV", 20, 5),
    ("MOD", 9, 4),
    ("ADD", 1, 2)
]

def execute_operation(operation, *args):
    if operation == "ADD":
        result = args[0] + args[1]
        print(f"AdDResult: {result}", flush=True)
    elif operation == "SUB":
        result = args[0] - args[1]
        print(f"SubResult: {result}", flush=True)
    elif operation == "MUL":
        result = args[0] * args[1]
        print(f"MulResult: {result}", flush=True)
    elif operation == "DIV":
        if args[1] != 0:
            result = args[0] / args[1]
            print(f"DivResult: {result}", flush=True)
        else:
            print("Error: Division by zero is not allowed", flush=True)
    elif operation == "MOD":
        result = args[0] % args[1]
        print(f"ModResult: {result}", flush=True)
        
def process_operation(operation, process_id):
    for op in operation:
        op_name, arg1, arg2 = op
        print(f"Process {process_id}: Performing {op_name} with argument {arg1} and {arg2}", flush=True)
        execute_operation(op_name, arg1, arg2)
        time.sleep(1)
        
thread1 = threading.Thread(target=process_operation, args=(process_1_operation, "1"))
thread2 = threading.Thread(target=process_operation, args=(process_2_operation, "2"))

thread1.start()
thread2.start()

thread1.join()
thread2.join()