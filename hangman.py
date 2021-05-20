def start(lgth,nl):
    global chance
    print('--------------------------------------------------------------------------------\n')
    print('\t\t\t\t\t\t\tChances left:',chance)
    alpha=input('\nEnter the letter(small letters only):')
    alp=list(alpha)
    i=0
    f=0
    while i<lgth:
       if nl[i]==alp[0]:
           print('\n\tLetter is present in position',i+1)
           f=1
       i+=1
    if f==0:
        print('\nLetter not present chance lost')
        chance-=1
        if chance==0:
            end(nl)
    ch=input('\nDid you find the word:(y/n):')
    if ch=='y':
        fw=input('\nEnter the word:')
        fw=str(fw)
        delimiter=''
        a=delimiter.join(nl)
        a=str(a)
        if a==fw:
            print('\nYOU WIN the word is:',fw)
            con=input('\nDo you want to continue(y/n)')
            if con=='y':
                chance=9
                main()
            else:
                exit()
        else:
            a=delimiter.join(nl)
            a=str(a)
            print('\nYOU LOST the word is:',a)
            con=input('\nDo you want to continue(y/n)')
            if con=='y':
                chance=9
                main()
            else:
                exit()
    elif ch=='n':
        start(lgth,nl)



def end(nl):
  global chance
  print('--------------------------------------------------------------------------------\n')
  print('YOU LOST\n')
  delimiter=''
  a=delimiter.join(nl)
  print('\nThe word is',a)
  print('''
    _______
    |      |
    ()     |
   <||>    |
   _/\_    |
           |

           ''')
  con=input('Do you want to continue(y/n)')
  if con=='y':
      chance=9
      main()
  else:
      exit()





def main():

  ran=['abruptly','lamentable' ,'replace','smoke','spectacular','memory','alcoholic','middle','telephone','polite','unique','flavor','discovery','sound']
  w=random.choice(ran)
  nl=list(w)
  lgth=len(nl)
  r=random.choice(range(lgth))
  print('\n--------------------------------------------------------------------------------')
  print('\t\t\t\tHANGMAN\n\n--------------------------------------------------------------------------------\n')
  c=input('Press 1 to start game and 0 to quit:')
  c=int(c)
  if c==1:
     print('\n\n\t\tHERE ARE THE HINTS OF YOUR WORD\n\t\t*******************************')
     time.sleep(.5)
     print('\n\n\tYour word has',lgth,'letters and the letter is:',nl[r])
     print('\n\tThe places where the letter:',nl[r],':occur is given below:\n')
     i=0
     while i<lgth:
        if nl[i]==nl[r]:
          print('\t',i+1)
        i+=1
     start(lgth,nl)
  if c==0:
     exit();
import random
import time
chance=9
main()
