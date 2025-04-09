import time

class Process:
    def __init__(self, operations, process_id):
        self.operations = operations
        self.process_id = process_id
        
    def execute(self):
        for operation in self.operations:
            op_name, arg1, arg2 = operation
            print(f"Process {self.process_id}: processing {op_name} with arguments {arg1} and {arg2}")
            self.execute_operation(op_name, arg1, arg2)
            
    def execute_operation(self, operation, arg1, arg2):
        if operation == "ADD":
            result = arg1 + arg2
            print(f"AddResult: {result}")
            time.sleep(0.3)
        elif operation == "SUB":
            result = arg1 - arg2
            print(f"SubResult: {result}")
            time.sleep(0.3)
        elif operation == "MUL":
            result = arg1 * arg2
            print(f"MulResult: {result}")
            time.sleep(0.3)
        elif operation == "DIV":
            if arg2 != 0:
                result = arg1 / arg2
                print(f"DivResult: {result}")
                time.sleep(0.3)
            else:
                print("Error: Division by zero is not allowed")
        elif operation == "MOD":
            result = arg1 % arg2
            print(f"ModResult: {result}")
            time.sleep(0.3)

process_1_operation =[
    ("ADD", 5, 3),
    ("SUB", 10, 2),
]

process_2_operation =[
    ("MULL", 6, 7),
    ("DIV", 8, 4),
    ("MOD", 8, 2),
]

process_1 = Process(process_1_operation, "1")
process_2 = Process(process_2_operation, "2")

process_1.execute()
time.sleep(0.5)
process_2.execute()