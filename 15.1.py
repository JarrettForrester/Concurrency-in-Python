#15.1 Use multiprocessing to create three separate processes. Make each one wait a random number of seconds between zero and one, print the current time, and then exit.
    
    import multiprocessing
    import random
    import time
    from datetime import datetime
    
    def process():
        wait_time = random.uniform(0, 1)
        time.sleep(wait_time)
        print(f\"Current time: {datetime.now()}\")
        return
  
    if __name__ == \"__main__\":
        processes = []
        for i in range(3):
            p = multiprocessing.Process(target=process)
            processes.append(p)
            p.start()
        for p in processes:
            p.join()

