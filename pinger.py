import concurrent.futures
import ping3

#ideas: Add a optional graph function maybe.

class pingdata:
    host=""
    maxpings=100

def do_ping(i):
    ping_time = ping3.ping(pingdata.host)
    if ping_time is None:
        print(f"Ping {i} failed!")
        return float('inf')
    #print(f"Ping {i} done: {ping_time:.3f}s") #Debugging.
    return ping_time

def run_pings(total_pings, max_threads):
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = [executor.submit(do_ping, i) for i in range(total_pings)]
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())
    return results

def init_ping(PingDataModule):
    pingdata.host=PingDataModule.host
    Y = 20  # max threads simultaneously
    print(f"Running {PingDataModule.maxpings} pings with max {Y} threads at once...\n")
    ping_times = run_pings(PingDataModule.maxpings, Y)

    filtered = [p for p in ping_times if p != float('inf')]
    if filtered:
        print("\nAll done!")
        print(f"Minimum Ping: {min(filtered):.3f}s")
        print(f"Maximum Ping: {max(filtered):.3f}s")
        print(f"Average Ping: {sum(filtered)/len(filtered):.3f}s\n")
        minping=f"{min(filtered):.3f}s"
        maxping=f"{max(filtered):.3f}s"
        avgping=f"{sum(filtered)/len(filtered):.3f}s"
        PingDataModule.last_ping=f"min ping: {minping}, max ping: {maxping}, avg ping: {avgping}"
    else:
        print("No successful pings!")
    return 

if __name__ == "__main__":
    pingdata.host=input("What host? ")
    if pingdata.host=="":
        pingdata.host="127.0.0.1"

    print("init amount")
    while True:
        try:
            pingdata.maxpings=int(input("How many?(don't do too many if slow internet) "))
            break
        except ValueError:
            print(f"Nope, that ain't a number.\n")
    print("done init")
    Y = 20  # max threads simultaneously
    print(f"Running {pingdata.maxpings} pings with max {Y} threads at once...\n")
    ping_times = run_pings(pingdata.maxpings, Y)

    filtered = [p for p in ping_times if p != float('inf')]
    if filtered:
        print("\nAll done!")
        print(f"Minimum Ping: {min(filtered):.3f}s")
        print(f"Maximum Ping: {max(filtered):.3f}s")
        print(f"Average Ping: {sum(filtered)/len(filtered):.3f}s")
    else:
        print("No successful pings!")
