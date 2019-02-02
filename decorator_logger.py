# Decorator
def param_logger(path: str):
      def logger(old_function):
            def new_function(*args, **kwargs):
                  from time import ctime
                  from datetime import date
                  from inspect import signature
            
                  launch_date = date.today()
                  launch_time = ctime()
                  func_name = old_function.__name__
                  func_args = list(signature(old_function).parameters.items())
                  func_output = old_function(*args, **kwargs)

                  data_to_write = [launch_date, launch_time, func_name, func_args, func_output]

                  with open(path, 'a') as f:
                        for data in data_to_write:
                              f.writelines(str(data) + '\n')
                  print (func_output)
            return new_function
      return logger

# Func to decorate
@logger
def text_updater (text, start = '', max_line = int(), in_file = False):
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

text_updater('hjkffl' , start = '!!!', max_line = 3, in_file = False)
