def divide(dividend, divisor):
    if divisor==0:
        raise ZeroDivisionError("Divisor Cannot be 0")
    
    return dividend/divisor


def calculate(*num,operator):
    return operator(*num)



print(calculate(21,2,operator=divide))

def search(sequence,expected,finder):
    for elem in sequence:
        if finder(elem)==expected:
            return elem
        
    raise RuntimeError(f"Could not find an element with {expected}")

friends=[
    {"name":"Rolf", "age":34},
    {"name": "Adam", "age": 21}
]

print(search(friends,"Rolf", lambda friend: friend["name"]))