import json

class Countries_iterator:
      def __init__(self, start, end):
            self.start = start
            self.end = end

      def __iter__(self):
            return self

      def __next__(self):
            self.start += 1
            if self.start == self.end:
                  raise StopIteration
            return self.start

      def open_file(self, file):
            loaded_file = ''
            with open(file, 'r', encoding = 'UTF8') as countries:
                  loaded_file = json.load(countries)
            return loaded_file

      def convert_to_dict(self, loaded_file):
            countries_dict = {}
            country_name = ''
            common_reference = 'https://en.wikipedia.org/wiki/'
            country_reference = ''
            for country in loaded_file:
                  country_name = country['name']['official']
                  country_reference = common_reference + country_name
                  countries_dict[country_name] = country_reference
            return countries_dict
                  

      def write_to_file(self, countries_dict):
            with open('countries_output.json', 'w') as outfile:
                  json.dump(countries_dict, outfile)
                  print('Completed')
                  
countries = Countries_iterator(1, 100)
loaded_file = countries.open_file('countries.json')
countries_dict = countries.convert_to_dict(loaded_file)
countries.write_to_file(countries_dict)


