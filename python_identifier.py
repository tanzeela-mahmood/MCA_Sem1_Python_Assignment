# Python program to demonstrate naming rules for identifiers

def identifier_rules():
    print("Python Identifier Naming Rules:")
    print("1. Identifiers can contain letters (a-z, A-Z), digits (0-9), and underscores (_).")
    print("2. Identifiers must begin with a letter or an underscore (_), but not a digit.")
    print("3. Identifiers are case-sensitive (e.g., 'Var' and 'var' are different).")
    print("4. Identifiers cannot be a reserved keyword in Python.")
    print("5. Identifiers can be of any length.")
    print("6. Special characters (e.g., @, $, %, etc.) are not allowed.")
    print("7. Identifiers should not start with numbers or contain spaces.")
    print()

# Demonstrating valid and invalid identifiers

def valid_identifiers():
    print("Examples of Valid Identifiers:")
    _var = 10
    print("1. _var (starts with an underscore)")
    var123 = 20
    print("2. var123 (letters followed by digits)")
    my_var = 30
    print("3. my_var (contains an underscore)")
    myVar = 40
    print("4. myVar (camelCase style)")
    print()

def invalid_identifiers():
    print("Examples of Invalid Identifiers:")
    print("1. 123var (starts with a digit)")
    print("2. my-var (contains a hyphen)")
    print("3. my var (contains a space)")
    print("4. for (reserved keyword)")
    print()

# Reserved keywords in Python

def reserved_keywords():
    import keyword
    print("Reserved Keywords in Python:")
    print(keyword.kwlist)
    print()

# Main function
if __name__ == "__main__":
    identifier_rules()
    valid_identifiers()
    invalid_identifiers()
    reserved_keywords()
