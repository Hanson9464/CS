print("Hello world")
name = "Hanson"
print(f"Hello {name}")
age = 16
print(f"Hello {age}")

if age < 18:
    print("You're a minor")
elif age < 21:
    print("You can not drink alcohol in the US")
else:
    print("You can do anything")

if __name__ == "__main__":
    print("this only executes when we execute this file")
