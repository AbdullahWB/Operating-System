import threading
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
            
    def process_operation(self, operations, process_id):
        for operation in operations:
            op_name, arg1, arg2 = operation
            print(f"Process {process_id}: Performing {op_name} with arguments {arg1} and {arg2}")
            self.execute(op_name, arg1, arg2)




thread1 = threading.Thread(target=process_operation, args=(process_1_opreration, "1"))
thread1 = threading.Thread(target=process_operation, args=(process_2_opreration, "2"))

thread1.start()
thread2.start()

thread1.join()
thread2.join()