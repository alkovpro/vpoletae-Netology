class Timer:
   
    def __init__(self, file_name):
        self.file = file_name
        self.open = open(file_name, encoding = 'UTF8')

    def __enter__(self):
        import time
        from pprint import pprint
        start_time_int = time.time()
        start_time_str = time.ctime()
        
        if self.file.endswith('.json'):
            import json
            data_to_measure = json.load(self.open)
            pprint (data_to_measure)

        elif self.file.endswith('.yaml'):
            import yaml
            data_to_measure = yaml.load(self.open)
            pprint (data_to_measure)

        else:
            print ('Not .json or .yaml')

        print ('Start time: {}'.format(start_time_str))
        print ('End time: {}'.format(time.ctime()))
        print ('Duration: {}'.format(round(time.time() - start_time_int), 2))
        
    def __exit__(self, *args):
        self.open.close()

