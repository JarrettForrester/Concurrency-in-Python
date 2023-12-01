#13.2 Read the text file today.txt into the string today_string.
    
    from datetime import datetime
    
    with open('today.txt', 'r') as file:
        today_string = file.read()
   
  
