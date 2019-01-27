class Hash_iterator:
      def __init__(self, start, end, path):
            self.start = start
            self.end = end
            self.path = path

      def __iter__(self):
            return self

      def __next__(self):
            self.start += 1
            if self.start == self.end:
                  raise StopIteration
            return self.start

      def hash_line(self):
            loaded_lines = []
            hashed_lines = []
            with open(self.path, 'r', encoding = 'UTF8') as infile:
                  loaded_lines = infile.readlines()
            for line in loaded_lines:
                  hashed_lines.append(hash(line))
            print (hashed_lines)

hasher = Hash_iterator(1, 10, 'C:\Vadim\Personal\PY_code\Netology\Generator. Yield\lines.txt')

for i in hasher:
      hasher.hash_line()
            



