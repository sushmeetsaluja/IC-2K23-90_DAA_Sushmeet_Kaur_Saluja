# Tasks arrive in this order
tasks = ["Task1", "Task2", "Task3", "Task4", "Task5"]

print("Tasks:", tasks)


# -------------------------
# Stack - LIFO
# -------------------------

stack = []

# Add tasks to the stack
for task in tasks:
    stack.append(task)

print("\nStack order (LIFO):")

# Last task added is removed first
while stack:
    task = stack.pop()
    print(task)


# -------------------------
# Queue - FIFO
# -------------------------

queue = []

# Add tasks to the queue
for task in tasks:
    queue.append(task)

print("\nQueue order (FIFO):")

# First task added is removed first
while queue:
    task = queue.pop(0)
    print(task)


# -------------------------
# Printer Queue
# -------------------------

printer_queue = tasks.copy()

print("\nPrinter should use: Queue")
print("Printing order:")

while printer_queue:
    job = printer_queue.pop(0)
    print(job)