#13.3 Parse the date from today_string.
    
    from datetime import datetime
    
    with open(\"today.txt\", \"r\") as f:
        today_string = f.read()
   
    today = datetime.strptime(today_string, \"%m/%d/%Y\").date()
   
  
