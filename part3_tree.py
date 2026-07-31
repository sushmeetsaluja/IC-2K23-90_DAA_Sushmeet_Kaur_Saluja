# Part 3 - Build a Small Tree

# Top level subjects
math = ["Algebra", "Geometry"]
science = ["Physics", "Chemistry"]

print("Subject Tree:")

print("\nMath")
print("  Algebra")
print("  Geometry")

print("\nScience")
print("  Physics")
print("  Chemistry")


# Level order traversal

print("\nLevel Order Traversal:")

print("Math", end=" -> ")
print("Science", end=" -> ")

for subject in math:
    print(subject, end=" -> ")

for subject in science:
    print(subject, end=" -> ")

print("End")