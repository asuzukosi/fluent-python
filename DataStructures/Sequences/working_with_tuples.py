from collections import namedtuple


City = namedtuple("City", ["name", "country", "population", "cordinate"])

new_york = City("New York", "USA", 36577, (23.45 , 56,3))
print(new_york.name)

# using the _make and _asdict methods in the named tuple class

delhi = City._make(('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)))
print(delhi)
print(dict(delhi._asdict()))
print(City._fields)
# this can be used to store data when performing data science and ai tasks