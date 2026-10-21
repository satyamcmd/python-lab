values = input("Enter frozen set elements separated by spaces: ").split()
frozen_items = frozenset(values)

print("Frozen set:", frozen_items)
print("Is 'a' in the frozen set?", "a" in frozen_items)
print("Frozen set can be used as a dictionary key:", {frozen_items: "value"})
print("Has an add method:", hasattr(frozen_items, "add"))
