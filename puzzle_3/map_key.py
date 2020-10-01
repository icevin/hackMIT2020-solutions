import json

def round( n ): 
  
    # Smaller multiple 
    a = (n // 10) * 10
      
    # Larger multiple 
    b = a + 10
      
    # Return of closest of two 
    return (b if n - a > b - n else a) 

with open('keymap.json') as keymap:
    data = json.load(keymap)
    while True:
        test = int(input())
        print(data[str(round(test))])

    