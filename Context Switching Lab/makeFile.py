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


