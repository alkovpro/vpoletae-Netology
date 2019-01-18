# creating class Contact
class Contact:
      def __init__(self, name, surname, phone, pref_contact = False, *args, **kwargs):
            self.name = name
            self.surname = surname
            self.phone = phone
            self.pref_contact = pref_contact
            self.tuple = args
            self.dict = kwargs

      def __str__(self):
            print('''
Name: {0}
Surname: {1}
Phone number: {2}
Prefferable: {3}
Additional information:'''.format(str(self.name), str(self.surname), str(self.phone), str(self.pref_contact)))
            for key, value in self.dict.items():
                  print('\t{0} : {1}'.format(key, value))


# creating class PhoneBook
class PhoneBook:
      def __init__(self, name):
            self.name = name
            self.contacts = []

      def add_contact(self, contact):
            self.contacts.append(contact)

      def show_contacts(self):
            for contact in self.contacts:
                  contact.__str__()

      def del_contact(self, phone_number):
            counter = int()
            for contact in self.contacts:
                  if contact.phone == phone_number:
                        self.contacts.remove(contact)
                        counter += 1
                        break
                  else:
                        pass
            if counter == 0: print('No such phone number!')

      def find_preffered(self):
            pref_list = {}
            for contact in self.contacts:
                  if contact.pref_contact:
                        pref_list[contact.name] = contact.pref_contact
            print('The list of prefferables:')
            for key, value in pref_list.items():
                  print('{0} : {1}'.format(key, value))
      

      def name_surname_find(self, name, surname):
            counter = int()
            for contact in self.contacts:
                  if name.lower() == contact.name.lower() and surname.lower() == contact.surname.lower():
                        contact.__str__()
                        counter += 1
                        break
                  else:
                        pass
            if counter == 0: print('No such contact!')
            

# launching programm
vadim = Contact('Vadim', 'Poletaev', '1', False, email = 'poletaevvb@mail.ru')
vasia = Contact('Vasia', 'Ivanov', '2', '2', email = 'ivanov@mail.ru')
petya = Contact('Petya', 'Petrov', '3', False, email = 'petrov@mail.ru')

list_of_contacts = [vadim, vasia, petya]

book = PhoneBook('MyBook')
for contact in list_of_contacts:
      book.add_contact(contact)

book.show_contacts()

book.del_contact('2')

book.show_contacts()

book.find_preffered()

book.name_surname_find('Vadim', 'Poletaev')







