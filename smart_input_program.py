def categorize_age(age):
    if age < 13:
        return "Child"
    elif age < 20:
        return "Teenager"
    elif age < 60:
        return "Adult"
    else:
        return "Senior Citizen"

def main():
    print("----- Smart Input Program -----")

    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    hobby = input("Enter your hobby: ")

    category = categorize_age(age)

    print("\n----- Personalized Message -----")
    print(f"Hello {name}! 😊")
    print(f"You are categorized as: {category}.")
    print(f"It's wonderful that you enjoy {hobby}. Keep pursuing your passion!")

main()