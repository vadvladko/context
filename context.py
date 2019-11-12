import time

start = time.time()


class Company:

  def __init__(self, firma):
    self.f = open(firma)
      

  def __enter__(self):

    lines = self.f.read()
    rezult = lines.split()
    return (len(rezult))

  def __exit__(self, exc_type, exc_val, exc_tb):

    
    self.f.close()
    finish = time.time()
    
    time_rezult = finish - start
    print('Программа выполнялась: ' + str(time_rezult) + ' секунд')  
         

with Company('text.txt') as company_file:
  print(company_file)
