age = int(input("Enter your age: "))

# 8.   • 'You are a child' if age < 13
# 9.   • 'You are a teenager' if 13 ≤ age < 18
# 10.   • 'You are an adult' if 18 ≤ age < 60
# 11.   • 'You are a senior citizen' if age ≥ 60

if age < 13:
    print("You are a child")
elif 13 <= age < 18:
    print("You are a teenager")
elif 18 <= age < 60:
    print("You are an adult")
elif age >= 60:
    print("You are senior citizen")