
# Using the getitem dunder method to operate on a python object
class GetObjectTester:
    """
    The getitem syntax is used in native data types in the python language such as:
    * iterators
    * lists
    * operator overloading
    * attribute access
    * dictionaries
    
    etc
    """
    def __getitem__(self, value):
        return str(value) + " from kosi's object"



if __name__ == "__main__":
    # initiate the method if the file is called
    sample_object = GetObjectTester()
    print(sample_object["hello"])