file_list = ["without/File1.txt", "without/File2.txt", "without/File3.txt", "without/File4.txt"]

file_contents = {
    "without/File1.txt": [
        ("ADD", 10, 5, "AddResult"),
        ("SUB", 30, 4, "SubResult")
    ],
    "without/File2.txt": [
        ("MUL", 3, 6, "MulResult"),
        ("DIV", 10, 2, "DivResult"),
        ("MOD", 15, 5, "ModResult")
    ],
    "without/File3.txt": [
        ("DIV", 10, 2, "DivResult"),
        ("MOD", 15, 5, "ModResult"),
        ("MUL", 34, 4, "MulResult")
    ],
    "without/File4.txt": [
        ("ADD", 44, 6, "AddResult"),
        ("SUB", 30, 4, "SubResult"),
        ("MUL", 34, 4, "MulResult"),
        ("DIV", 34, 8, "DivResult")
    ]
}

for file_path in file_list:
    with open(file_path, "w") as f:
        lines = file_contents.get(file_path, [])
        for operation, op1, op2, result in lines:
            f.write(f"{operation} {op1} {op2} {result}\n")
        print(f"File {file_path} created")



class Process:
    def __init__(self, operations, process_id):
        self.operations = operations
        self.process_id = process_id
        
    def execute(self):
        for operation in self.operations:
            op_name, arg1, arg2 = operation
            print(f"Process {self.process_id}: Performing {op_name} with argument {arg1} and {arg2}")
            self.execute_operation(op_name, arg1, arg2)
    
    def execute_operation(self , operation, arg1, arg2):
        if operation == "ADD":
            result = arg1 + arg2
            print(result)
        elif operation == "SUB":
            result = arg1 - arg2
            print(result)
        elif operation == "MUL":
            result = arg1 * arg2
            print(result)
        elif operation == "DIV":
            if arg2 != 0:
                result = arg1 / arg2
                print(result)
            else:
                print("Error")
        elif operation == "MOD":
            result = arg1 % arg2
            print(result)


processes = []
for i, file_path in enumerate(file_list, start=1):
    try:
        with open(file_path, "r") as f:
            operations = []
            for line in f:
                parts = line.strip().split()
                if len(parts) >= 3:
                    op_name = parts[0]
                    try:
                        arg1 = int(parts[1])
                        arg2 = int(parts[2])
                        operations.append((op_name, arg1, arg2))
                    except ValueError:
                        print(f"Error: Invalid arguments in {file_path}: {line.strip()}")
            process = Process(operations, process_id=i)
            processes.append(process)
    except FileNotFoundError:
        print(f"Error: File {file_path} not found")
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

for process in processes:
    print(f"\nExecuting Process {process.process_id}:")
    process.execute()