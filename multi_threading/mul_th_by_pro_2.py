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

# Sample operations for process 1 and process 2
process_1_operations = [("ADD", 5, 3), ("MUL", 6, 2), ("DIV", 8, 4)]
process_2_operations = [("SUB", 9, 4), ("MOD", 10, 3), ("ADD", 7, 6)]

# Create Process instances
process1 = Process(process_1_operations, "1")
process2 = Process(process_2_operations, "2")

# Thread creation for process execution
thread1 = threading.Thread(target=process1.execute)
thread2 = threading.Thread(target=process2.execute)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("All processes have finished.")
