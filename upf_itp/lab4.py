'''
Introduction to Programming
2018-19 First Trimester
Lab 4 - Dictionaries

Objective
The objective of this lab is to implement an agenda using lists and
dictionaries. This agenda, which must be implemented using a dictionary, will
have a key (the user's name), and will containing the following information for
each user:

N phone numbers (where N can be any integer >= 0)
N email accounts (where N can be any integer >= 0)
1 postal address

Address will be a dictionary, with 4 keys
("street", "number", "zip code" and "city").
'''
import re

# Returns an integer from the user input
def get_int_from_input(msg):
  while True:
    try:
      return int(input(msg))
    except ValueError:
      print('Please enter a valid integer value')

# Returns an integer betwen a and b (included) from the user input
def get_option(a, b, msg='Select an option: '):
  option = get_int_from_input(msg)
  while option < a or option > b:
    option = get_int_from_input('Invalid input. Try again: ')
  return option

# Returns a valid string from input that matches the given regular expression
def get_input_matches_regex(msg, regex):
  pattern = re.compile(regex)
  user_input = input('Enter the {}: '.format(msg))
  while not pattern.match(user_input):
    user_input = input('Invalid {}. Try again: '.format(msg))
  return user_input

# The a single valid letter
def get_valid_letter():
  return get_input_matches_regex('letter', r'^[a-zA-Z]{1}$')

# Return a string that only contains characters a to z
def get_valid_substring():
  return get_input_matches_regex('substring', r'^[a-zA-Z]+$')

# Return a string that only contains digits and is between 1 and 9 digits long
def get_valid_numerical_substring():
  return get_input_matches_regex('substring', r'^\d{1,9}$')

# The name of the contact is NOT an empty string
def get_valid_name():
  return get_input_matches_regex('contact name', r'^[a-zA-Z ]+$')

# The email address contains the characters @ and. (in this order)
def get_valid_email():
  return get_input_matches_regex('email', r'^[\w\.]+@[\w\.]+\.[a-zA-Z]{2,3}$')

# The telephone number (which should be a string), contains exactly 9 digits
def get_valid_phone_number():
  return get_input_matches_regex('phone number', r'^[1-9]\d{8}$')

# The name of the street is NOT an empty string
def get_valid_street():
  return get_input_matches_regex('street name', r'^[a-zA-Z/\\ ]+$')

# The street number is a positive integer
def get_valid_street_number():
  return int(get_input_matches_regex('street number', r'^[1-9]\d{,4}$'))

# The zip code (should be a string), contains exactly 5 digits.
def get_valid_zipcode():
  return get_input_matches_regex('zip code', r'^\d{5}$')

# The name of the city DOES NOT contain digits and is NOT an empty string
def get_valid_city_name():
  return get_input_matches_regex('city name', r'^[a-zA-Z\' ]+$')

# Prints in a visual format the given contact information
def print_contact(name, info):
  phones  = ', '.join(info[0])
  emails  = ', '.join(info[1])
  address = ', '.join([str(val) for val in info[2].values()])
  print('Contact: {}\n  Phones: {}\n  Emails: {}\n  Address: {}\n'
    .format(name, phones, emails, address))

# Returns a list of phone numbers
def get_phone_list():
  number = get_option(0, 10, msg='How many phones will you enter?: ')
  return [get_valid_phone_number() for _ in range(number)]

# Returns a list of email addresses
def get_email_list():
  number = get_option(0, 10, msg='How many emails will you enter?: ')
  return [get_valid_email() for _ in range(number)]

# Return a valid address
def get_valid_address():
  return {
    'street': get_valid_street(), 
    'number': get_valid_street_number(), 
    'zipcode': get_valid_zipcode(), 
    'city': get_valid_city_name()
  }

# Creates a new contact from the user input and adds it to the agenda
def new_contact(agenda):
  name = get_valid_name()
  if name in agenda:
    print('The contact {} already exists.'.format(name))
    return
  phones = get_phone_list()
  emails = get_email_list()
  address = get_valid_address()
  agenda[name] = [phones, emails, address]
  print('Contact {} added successfully.'.format(name))

# Allows the user to add or remove a phone number of a given contact
def modify_phone_list(agenda, name):
  # A tupple containing the menu options
  menu_options = (
    'Add phone number',
    'Delete phone number',
    'Print menu',
    'Back'
  )
  # The number of total options
  total_options = len(menu_options)
  # Print the menu options
  print_menu(menu_options)
  # While option isn't exit get an option and execute the corresponding function
  while True:
    option = get_option(1, total_options,
      'Select an option ({} for printing the menu): '.format(total_options-1))
    if option == total_options-1: print_menu(menu_options)
    elif option == total_options: break
    elif option == 1: agenda[name][0].append(get_valid_phone_number())
    elif option == 2:
      phone_list = agenda[name][0]
      if phone_list:
        print_menu(phone_list)
        sub_option = get_option(1, len(phone_list),
          'Select a phone number to delete: ')
        deleted_phone = phone_list.pop(sub_option-1)
        print('Phone {} deleted successfully'.format(deleted_phone))
      else:
        print('No phone numbers to show')
  # Notify when we exit the menu
  print('Exit modify phone list sub-menu')

# Allows the user to add or remove a email address of a given contact
def modify_email_list(agenda, name):
  # A tupple containing the menu options
  menu_options = (
    'Add email address',
    'Delete email address',
    'Print menu',
    'Back'
  )
  # The number of total options
  total_options = len(menu_options)
  # Print the menu options
  print_menu(menu_options)
  # While option isn't exit get an option and execute the corresponding function
  while True:
    option = get_option(1, total_options,
      'Select an option ({} for printing the menu): '.format(total_options-1))
    if option == total_options-1: print_menu(menu_options)
    elif option == total_options: break
    elif option == 1: agenda[name][1].append(get_valid_email())
    elif option == 2:
      email_list = agenda[name][1]
      if email_list:
        print_menu(email_list)
        sub_option = get_option(1, len(email_list),
          'Select a email address to delete: ')
        deleted_email = email_list.pop(sub_option-1)
        print('Email {} deleted successfully'.format(deleted_email))
      else:
        print('No email addresses to show')
  # Notify when we exit the menu
  print('Exit modify email list sub-menu')

# Allows the user to modify a single field of the address field
def modify_address(agenda, name):
  # A tupple containing the menu options
  menu_options = (
    'Modify street',
    'Modify street number',
    'Modify zip code',
    'Modify city',
    'Print menu',
    'Back'
  )
  # The number of total options
  total_options = len(menu_options)
  # A tupple containing the corresponding functions to the menu options
  menu_functions = (
    get_valid_street,
    get_valid_street_number,
    get_valid_zipcode,
    get_valid_city_name
  )
  # Address fields
  fields = ('street', 'number', 'zipcode', 'city')
  # Print the menu options
  print_menu(menu_options)
  # While option isn't exit get an option and execute the corresponding function
  while True:
    option = get_option(1, total_options,
      'Select an option ({} for printing the menu): '.format(total_options-1))
    if option == total_options-1: print_menu(menu_options)
    elif option == total_options: break
    else:
      value = menu_functions[option-1]()
      agenda[name][2][fields[option-1]] = value
  # Notify when we exit the menu
  print('Exit modify address sub-menu')

# Modifies the data of an existing contact
def modify_contact(agenda):
  name = get_valid_name()
  if not name in agenda:
    print('Contact {} doesn\'t exists'.format(name))
    return
  # A tupple containing the menu options
  menu_options = (
    'Modify phone list',
    'Modify email list',
    'Modify address',
    'Print contact info',
    'Print menu',
    'Back'
  )
  # The number of total options
  total_options = len(menu_options)
  # A tupple containing the corresponding functions to the menu options
  menu_functions = (
    modify_phone_list,
    modify_email_list,
    modify_address,
  )
  # Print the contact information and the menu
  print_contact(name, agenda[name])
  print_menu(menu_options)
  # While option isn't exit get an option and execute the corresponding function
  while True:
    option = get_option(1, total_options,
      'Select an option ({} for printing the menu): '.format(total_options-1))
    if   option == total_options-2: print_contact(name, agenda[name])
    elif option == total_options-1: print_menu(menu_options)
    elif option == total_options: break
    else: menu_functions[option-1](agenda, name)
  print('Exit modify contact sub-menu')

# Ask a contact name and deletes it form the agenda
def delete_contact(agenda):
  name = get_valid_name()
  try:
    del agenda[name]
    print('Contact {} deleted'.format(name))
  except KeyError:
    print('Contact {} doesn\'t exists'.format(name))

# Ask a contact name and prints the information
def view_contact(agenda):
  name = get_valid_name()
  try:
    print_contact(name, agenda[name])
  except KeyError:
    print('Contact name doesn\'t exists')

# Prints the information of all contacts
def list_contacts(agenda):
  for name in agenda:
    print_contact(name, agenda[name])
  print('{} contacts listed.'.format(len(agenda)))

# Prints the contacts of a specific city
def list_contacts_city(agenda):
  city = get_valid_city_name()
  found = 0
  for name in agenda:
    info = agenda[name]
    if info[2]['city'] == city:
      found += 1
      print_contact(name, info)
  print('{} contacts from {} found.'.format(found, city))

# Prints the contacts of a specific zip code
def list_contacts_zipcode(agenda):
  zipcode = get_valid_zipcode()
  found = 0
  for name in agenda:
    info = agenda[name]
    if info[2]['zipcode'] == zipcode:
      found += 1
      print_contact(name, info)
  print('{} contacts from {} found.'.format(found, zipcode))

# Prints the contacts that starts with a specific letter
def list_contacts_name_starts(agenda):
  letter = get_valid_letter()
  found = 0
  for name in agenda:
    if letter.lower() == name[0].lower():
      found += 1
      print_contact(name, agenda[name])
  print('{} contacts starting with \'{}\' found.'.format(found, letter))

# Prints the contacts that containg a specific substring
def list_contacts_name_contains(agenda):
  substring = get_valid_substring()
  found = 0
  for name in agenda:
    if substring.lower() in name.lower():
      found += 1
      print_contact(name, agenda[name])
  print('{} contacts containing \'{}\' found.'.format(found, substring))

# Prints the contacts that contains a specific numerical substring in any of
# their phone numbers
def list_contacts_phone_contains(agenda):
  phone_substring = get_valid_numerical_substring()
  found = 0
  for name in agenda:
    info = agenda[name]
    for phone in info[0]:
      if phone_substring in phone:
        found += 1
        print_contact(name, info)
        break
  print('{} contacts containing \'{}\' found.'.format(found, phone_substring))

# Prints the contacts with exactly N phone numbers
def list_contacts_phones(agenda):
  number = get_option(0, 10, msg='Select the number of phone numbers: ')
  found = 0
  for name in agenda:
    info = agenda[name]
    if len(info[0]) == number:
      found += 1
      print_contact(name, info)
  print('{} contacts with {} phone numbers found.'.format(found, number))

# Prints the contacts with exactly N email addresses
def list_contacts_emails(agenda):
  number = get_option(0, 10, msg='Select the number of email addresses: ')
  found = 0
  for name in agenda:
    info = agenda[name]
    if len(info[1]) == number:
      found += 1
      print_contact(name, info)
  print('{} contacts with {} email addresses found.'.format(found, number))

# Prints the contacts with any email address that has a certain domain
def list_contacts_email_domain(agenda):
  domain = get_valid_substring()
  found = 0
  for name in agenda:
    info = agenda[name]
    for email in info[1]:
      if domain in email.split('.')[-1]:
        found += 1
        print_contact(name, info)
        break
  print('{} contacts containing \'{}\' found.'.format(found, domain))

# Prints the menu_options
def print_menu(menu_options):
  for i, menu_option in enumerate(menu_options):
    print('{:3d}. {}'.format(i+1, menu_option))

# The main function. It has the agenda dicctionaty with a few random generated
# contacts, the menu options and the menu work flow.
def main_menu():
  # An agenda containing 11 random generated contacts
  agenda = {
    'Christian Callau':[
      [
        '612345678',
        '631415926'
      ],
      [
        'christian.callau01@estudiants.upf.edu',
        'christiancallau@gmail.com'
      ],
      {
        'street':'Fake Street',
        'number':123,
        'zipcode':'08006',
        'city':'Springfield'
      }
    ],
    'Alejandro Fernandino':[
      [
        '734511278'
      ],
      [
        'alejandrofernandino29@hotmail.es',
        'alejandrofernandino48@yahoo.es'
      ],
      {
        'street':'Cecil Road',
        'number':527,
        'zipcode':'08005',
        'city':'Barcelona'
      }
    ],
    'Francisco Rubio':[
      [
        '839015313',
        '890998840',
        '803251681'
      ],
      [
        'franciscorubio@outlook.com',
        'franciscorubio@yahoo.es'
      ],
      {
        'street':'Manse Road',
        'number':764,
        'zipcode':'08006',
        'city':'Barcelona'
      }
    ],
    'Elsa Chicote':[
      [
        '850688824'
      ],
      [
        'elsachicote73@upf.edu',
        'elsachicote@hotmail.es'
      ],
      {
        'street':'Green Street',
        'number':624,
        'zipcode':'08006',
        'city':'Barcelona'
      }
    ],
    'Juan David Casas':[
      [
        '846754429'
      ],
      [
        'juandavidcasas67@upf.edu'
      ],
      {
        'street':'Dale Street',
        'number':506,
        'zipcode':'04007',
        'city':'Tarragona'
      }
    ],
    'Mariangel Collazo':[
      [
        '902253843'
      ],
      [
        'mariangelcollazo@gmail.com',
        'mariangelcollazo@yahoo.es'
      ],
      {
        'street':'Avondale Road',
        'number':770,
        'zipcode':'04007',
        'city':'Tarragona'
      }
    ],
    'Santino Cotilla':[
      [
        '973107377',
        '816112409',
        '742798950'
      ],
      [
        'santinocotilla@yahoo.es',
        'santinocotilla@hotmail.es',
        'santinocotilla@outlook.com'
      ],
      {
        'street':'Water Street',
        'number':278,
        'zipcode':'28002',
        'city':'Madrid'
      }
    ],
    'Isabela Alvarado':[
      [
        '995070457'
      ],
      [
        'isabelaalvarado07@yahoo.es',
        'isabelaalvarado29@outlook.com',
        'isabelaalvarado@upf.edu'
      ],
      {
        'street':'Manse Road',
        'number':510,
        'zipcode':'04007',
        'city':'Tarragona'
      }
    ],
    'Santiago Aguayo':[
      [
        '710744485'
      ],
      [
        'santiagoaguayo@gmail.com',
        'santiagoaguayo@upf.edu'
      ],
      {
        'street':'Vicarage Lane',
        'number':300,
        'zipcode':'08006',
        'city':'Barcelona'
      }
    ],
    'Eduardo Cadaval':[
      [
        '703152597',
        '662792598',
        '684593074',
        '742393729'
      ],
      [
        'eduardocadaval@upf.edu',
        'eduardocadaval@hotmail.es',
        'eduardocadaval81@gmail.com'
      ],
      {
        'street':'Dale Street',
        'number':619,
        'zipcode':'28001',
        'city':'Madrid'
      }
    ],
    'Manuela Saavedra':[
      [
        '931809511',
        '679224485',
        '692501540',
        '673860176'
      ],
      [
        'manuelasaavedra@hotmail.es',
        'manuelasaavedra46@gmail.com',
        'manuelasaavedra@upf.edu',
      ],
      {
        'street':'Dale Street',
        'number':610,
        'zipcode':'28002',
        'city':'Madrid'
      }
    ]
  }
  # A tupple containing the menu options
  menu_options = (
    'New contact',
    'Modify contact',
    'Delete contact',
    'View contact information',
    'List all contacts',
    'List contacts of specific city',
    'List contacts of specific zip code',
    'List contacts name starts with ...',
    'List contacts name contains ...',
    'List contacts phone contains ...',
    'List contacts with N phone numbers',
    'List contacts with N email accounts',
    'List contacts with certain domain email',
    'Print menu',
    'Exit'
  )
  # The number of total options
  total_options = len(menu_options)
  # A tupple containing the corresponding functions to the menu options
  menu_functions = (
    new_contact,
    modify_contact,
    delete_contact,
    view_contact,
    list_contacts,
    list_contacts_city,
    list_contacts_zipcode,
    list_contacts_name_starts,
    list_contacts_name_contains,
    list_contacts_phone_contains,
    list_contacts_phones,
    list_contacts_emails,
    list_contacts_email_domain
  )
  print_menu(menu_options)
  # While option isn't exit get an option and execute the corresponding function
  while True:
    option = get_option(1, total_options,
      'Select an option ({} for printing the menu): '.format(total_options-1))
    if option == total_options-1: print_menu(menu_options)
    elif option == total_options: break
    else: menu_functions[option-1](agenda)

# Call the main menu function to start the program
main_menu()
