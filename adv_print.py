def adv_print (*objects, start = '', max_line = int(), in_file = False):
      if max_line:
            print(start)
            counter = int()
            for obj in objects:
                  for elem in obj:
                        if counter + 1 == max_line:
                              print(elem, end = '\n')
                              counter = int()
                        else:
                              print(elem, end = '')
                              counter += 1
      else:
            print(start, *objects)

      if in_file:
            with open('output_file.txt', 'a') as f:
                  for obj in objects:
                        f.write(str(obj) + '\n')

adv_print((1,2,3), 'hjkffl' , max_line = 2, start = '!!!', in_file = True)
