import array

def covert_a_string_to_unicode_list_without_listcomp(text):
    result = []
    for t in text:
        result.append(ord(t))
        
    return result


def convert_a_string_to_unicode_list_with_listcomp(text):
    return [ord(v) for v in text]


def using_listcomp_to_generate_matrix_list_items():
    return [(color, size) for color in ["black", "white"] for size in ["M", "L", "S"]]

def using_generator_expressions_to_create_tuples_from_a_string(text):
    return tuple(ord(t) for t in text)


def using_generator_experessions_to_create_array_from_a_string(text):
    return array.array("I", (ord(t) for t in text))

def print_cartesian_product_of_a_list_of_shirt_sizes_and_colors():
    colors = ["black", "white", "red"]
    size = ["M", "L", "S"]
    for tshirt in (("%s %s" % (c, s)) for c in colors for s in size):
        print(tshirt)
    
if __name__ == "__main__":
    print(covert_a_string_to_unicode_list_without_listcomp("Hello"))
    print(convert_a_string_to_unicode_list_with_listcomp("Howdy"))
    print(using_listcomp_to_generate_matrix_list_items())
    print(using_generator_expressions_to_create_tuples_from_a_string("sample"))
    print(using_generator_experessions_to_create_array_from_a_string("sample"))
    print_cartesian_product_of_a_list_of_shirt_sizes_and_colors()
    
    # tuples aren't mutable, but lists are. But tuples can also be used for storing 
    # tables because they keep track of the position of the variable
    
    
    traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'),('ESP', 'XDA205856')]
    for country, _ in traveler_ids:
        print(country)
        
    # tuple unpacking in python
    name, school, age = ("John", "MIT", 20)
    print(name, school, age)
    
    
    # tuple unpacking to store excess values in a variable
    *rest, a, b = range(6)
    print(rest, a, b)