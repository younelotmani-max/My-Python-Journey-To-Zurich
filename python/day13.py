# ==========================================
# EX 1 (#047): Loop - while and else
# ==========================================
num = 1
while num <= 5:
    print(f"Number: {num}")
    num += 1
else:
    print("Loop Finished!")

print("=" * 40)

# ==========================================
# EX 2 (#048): Loop - while List Training
# ==========================================
friends = ["Ahmed", "Rayane", "Sara", "Amine"]
i = 0
while i < len(friends):
    print(f"Friend #{i + 1}: {friends[i]}")
    i += 1

print("=" * 40)

# ==========================================
# EX 3 (#049): Loop - while Task Manager
# ==========================================
tasks = []
max_tasks = 3
while max_tasks > 0:
    new_task = input("Enter a task: ").strip().capitalize()
    tasks.append(new_task)
    max_tasks -= 1
    print(f"Tasks left to add: {max_tasks}")

print(f"Your Final Tasks: {tasks}")
print("=" * 40)

# ==========================================
# EX 4 (#050): Loop - while Password Guess
# ==========================================
secret = "zurich123"
input_pass = input("Enter Secret Password: ").strip()

while input_pass != secret:
    print(" Wrong password! Try again.")
    input_pass = input("Enter Secret Password: ").strip()

print(" Access Granted!")
print("=" * 40)

# ==========================================
# EX 5 (#051): Loop - for with if
# ==========================================
numbers = [10, 25, 40, 55, 70]
for n in numbers:
    if n > 30:
        print(f"Number greater than 30: {n}")

print("=" * 40)

# ==========================================
# EX 6 (#052): Loop - for on Dictionary
# ==========================================
skills = {"Python": "90%", "SQL": "70%", "AI": "85%"}
for skill in skills:
    print(f"Skill: {skill} => Progress: {skills[skill]}")

print("=" * 40)

# ==========================================
# EX 7 (#053): Nested for Loops
# ==========================================
names = ["Younes", "Rayane"]
langs = ["Python", "C++"]

for name in names:
    print(f" {name} learns:")
    for lang in langs:
        print(f"  - {lang}")
        