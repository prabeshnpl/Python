import pandas as pd
import random
dataframe=pd.read_csv('D:\Backend\Backend\Github\hangman\datas.csv')
Random=random.randint(0,len(dataframe)-1)
print("\nHint: ",end='')
print(dataframe.iloc[Random,1],'\n')

word=dataframe.iloc[Random,0].upper()
length=len(word)
guessed=[None]*length
for x in range(length):
      guessed[x]='_ '
hang_man=int(0)


while hang_man!=7 and word!=''.join(guessed) :
     print(' '.join(guessed),': ',end='')
     alphabet=input("Guess the alphabet : ").upper()
     count=int(0)
     repeat=int(0)
     for x in range(length):
         if alphabet==word[x]:
            count=count+1
            for y in guessed:
                if alphabet==y:
                    repeat+=1
                    break
            guessed[x]=alphabet
            if repeat!=0:
                    print("Don't repeat same alphabet please\n\n")
                    continue
     if repeat!=0:
         continue            
     elif count==0:   
         hang_man+=1
         print("!!!Hangman drawn once!!!\n")
     else: 
         print('\n',' '.join(guessed),'\n')
else: 
     if hang_man==7:
       print(f"\n!!!Sorry you hanged!!!\nThe word was {word}")
     else:
         print("\nCongratulations you guessed the word correctly.")