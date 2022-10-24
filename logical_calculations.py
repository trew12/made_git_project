from logical_operations import logical_or, logical_and, logical_not


print(logical_or(True, False))
print(logical_not(True))
print(logical_and(True, False))
print(logical_not(logical_and(True, False)))
print(logical_not(logical_or(True, False)))
