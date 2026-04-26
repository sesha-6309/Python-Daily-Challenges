import copy

def create_inventory():
    inv = [
        {
            "item": "Laptop",
            "details": {
                "price": 50000,
                "stock": 10,
                "supplier": {"rating": 4.5}
            }
        },
        {
            "item": "Phone",
            "details": {
                "price": 20000,
                "stock": 25,
                "supplier": {"rating": 4.2}
            }
        }
    ]
    return inv


def apply_discount(data, roll_no):
    size = len(data)
    index = roll_no % size   # selecting item based on roll number

    for i in range(size):

        # reducing price by 10%
        data[i]["details"]["price"] = data[i]["details"]["price"] * 0.9

        # changing stock only for one item
        if i == index:
            data[i]["details"]["stock"] = data[i]["details"]["stock"] - 5

    return data



def compare_data(original, modified):
    ch = 0
    unch = 0

    print("\nDifferences:")

    for i in range(len(original)):
        if original[i] == modified[i]:
            unch += 1
        else:
            ch += 1
            print("Changed at index", i)
            print("Original:", original[i])
            print("Modified:", modified[i])
            print()

    return (ch, unch)


original = create_inventory()


shallow = copy.copy(original)
deep = copy.deepcopy(original)

roll_no = 7   # change to your actual roll number

# applying changes
apply_discount(shallow, roll_no)
apply_discount(deep, roll_no)

# printing results
print("\nOriginal data:")
print(original)

print("\nShallow copy data:")
print(shallow)

print("\nDeep copy data:")
print(deep)

# comparison
print("\nOriginal vs Shallow:")
res1 = compare_data(original, shallow)

print("\nOriginal vs Deep:")
res2 = compare_data(original, deep)

print("\nFinal result:")
print("Shallow:", res1)
print("Deep:", res2)