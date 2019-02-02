from utils import decorator_logger, hash_iterator, context_manager

logger = decorator_logger.logger

@logger
def text_updater(text, start = '', max_line = int(), in_file = False):
      word = ''
      if max_line:
            word += start
            counter = int()
            for letter in text:
                  if counter + 1 == max_line:
                        word += letter
                        break
                  else:
                        word += letter
                        counter += 1
            return word
      else:
            word += start
            word += text
            return word

      if in_file:
            with open('output_file.txt', 'a') as f:
                  for obj in objects:
                        f.write(str(obj) + '\n')


if __name__== '__main__':
      word = text_updater('hjkffl' , start = '!!!', max_line = 3, in_file = False)
      print(word)

      hasher = hash_iterator.Hash_iterator(1, 10)
      hasher.hash_elem(word)

      timer = context_manager.Timer('log_file.txt')
      timer.__enter__()
      timer.__exit__()
      

