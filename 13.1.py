#13.1 Write the current date as a string to the text file today.txt.
   
    from datetime import datetime
    
    now = datetime.now()
    date_string = now.strftime(\"%m/%d/%Y %H:%M:%S\")
    with open(\"today.txt\", \"w\") as file:
        file.write(date_string)
   
