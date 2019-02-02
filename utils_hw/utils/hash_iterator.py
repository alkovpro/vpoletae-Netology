class Hash_iterator:
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

      def hash_elem(self, iterable):
            for elem in iterable:
                  yield hash(elem)


