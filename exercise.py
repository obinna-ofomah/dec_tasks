###############################################################################################
# TASK 1A

def return_first_name(list_object:list):
    """
    A function that returns the first name of participants
    Args:
        A list of student's fullnames
    Return:
        A list of first names only
    """
    first_names = []

    for fullname in list_object:
        # Split the fullname into first_name and last_name
        firstname = fullname.split(' ')[0]
        first_names.append(firstname)

    return first_names

students = ['Obinna Ofomah', 'Chigozie Obasi', 'Amaka Eze', 'Toluwago Ernest']

# TASK 1B

def return_last_name(list_object:list):
    """
    A function that returns the lastname of every participant in a list
    Args:
        A list of participants' fullnames
    Return:
        A list of participants' lastnames
    """
    last_names = []

    for fullname in list_object:
        lastname = fullname.split(' ')[1]
        last_names.append(lastname)

    return last_names

# TASK 1C

def concat_names(list_object: list):
    """
    A function that concatenate the first and last names of students in a list
    Args:
        A list of students' fullnames
    Return:
        concatenated names
    """
    concat_names = []
    first_names = return_first_name(list_object)
    last_names =  return_last_name(list_object)

    for index in range(len(list_object)):
        concat_names.append(f'My full_name is {first_names[index]} {last_names[index]}')
    
    return concat_names


############################################################################################

# TASK 2

def transform_attributes(list_object):
    """
    A function that transforms attributes in a list
    Args:
        A list of attributes
    Return:
        A list of transformed attributes
    """
    transformed_elements  = []
    for element in list_object:
        # transform each element using the str.replace() method
        transformed_elements.append(element.replace(' ', '_'))

    return transformed_elements


##############################################################################################
# TASK 3

def extract_names(list_object):
    """
    A function that extract participant's name based on a set of conditions:
        --  The name must start with a capital letter
        --  The name must end with a letter 'a'

    Args:
        A list of participant's names
    Return:
        A list of participants' names that met the set condition
    """
    extracted_names = []
    for name in list_object:
        if name[0].isupper():
            if name.endswith('a'):
                extracted_names.append(name)
            elif name.endswith('e'):
                manipulated_name = name[:-1]+'a'
                extracted_names.append(manipulated_name)
            else:
                pass

    return extracted_names


#############################################################################################
# Task 4

def check_valid_alpha(list_object):
    """
    A function that checks a valid name in a list

    Args:
        A list of students' names
    Return:
        A list of valid names
    """
    valid_names = []
    for name in list_object:
        if not name.isalpha():
            raise ValueError(f'{name} is not a valid name, please cross check')
        else:
            valid_names.append(name)

    return valid_names

names = ['Obinna', 'Amae4tula', 'Chioma']

