import random
import threading
import time



def first_3_numbers():
    length = random.randint(3, 3) 
    eval = "1","2","3","4","5","6","7","8","9","0"


    return ''.join(random.choice(eval) for i in range(length))


def last_4_numbers():
    length = random.randint(4, 4) 
    eval = "1","2","3","4","5","6","7","8","9","0"


    return ''.join(random.choice(eval) for i in range(length))


def main():
    
    first_part = ["917","973","646","93","355","213","376","244","672","54","374","297","61","43","994"]
    random_first_part = random.choice(first_part)

    
    final_number = "+" + "(" + random_first_part + ")" + first_3_numbers() + "-" + last_4_numbers() 


    print(final_number)

    f1 = open("numbers.txt", "a+")
    f1.write(f"{final_number}\n")
    f1.close
    


threads=[]


for i in range(100000):
  t = threading.Thread(target = main)
  t.Daemon = True
  threads.append(t)

for i in range(100000):
  threads[i].start()
  time.sleep(0.2)

for i in range(100000):
  threads[i].join()
