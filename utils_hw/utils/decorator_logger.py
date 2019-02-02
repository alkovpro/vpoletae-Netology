# Decorator
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

            with open('log_file.txt', 'a') as f:
                  for data in data_to_write:
                        f.writelines(str(data) + '\n')
            return func_output
      return new_function

