
def checkCollatz(val:int)->None:
    
    assert(val>0), "Please input a positive integer"

    step=0        #Counts step
    while(val!=1):
      d=val%10    #Last digit
      val = (val*3+1) if d%2 else val//2
      step+=1
      #print(val)  #Prints the new value
    
    print()
    print('Checking complete, the sequence ended in a 4,2,1 loop.')  
    print(f'Number of steps taken:{step}')
    print('Uncomment print(val) at line 11 to see the values.\n')  


def inputCollatz()->int:
      
      try:
        number = int(input("Enter number to be checked- "))
        return number

      except(ValueError):
        raise ValueError("Input must be an integer")
      

            
if __name__ == "__main__":
    
    num = inputCollatz()
    checkCollatz(num)

