import argparse

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--data-file', type=str, default='Data/easy.txt',
                    help='Process data input into the student and marker file')
args = parser.parse_args()

# Process class to store details of each process
class Process:
    def __init__(self, name, runtime, arrival, io_freq):
        self.name = name
        self.runtime = runtime
        self.arrival = arrival
        self.io_freq = io_freq
        self.remaining_time = runtime
        self.completed = False
        self.next_io_time = io_freq if io_freq > 0 else None
        self.io_counter = 0  # Tracks when the next I/O event occurs


# Function to parse input and create Process objects
def parse_input(input_text):
    lines = input_text.strip().split("\n")
    num_processes = int(lines[0])
    processes = []
    for i in range(1, num_processes + 1):
        name, runtime, arrival, io_freq = lines[i].split(',')
        processes.append(Process(name, int(runtime), int(arrival), int(io_freq)))
    return processes


# The main scheduler logic
def scheduler(processes):
    time = 0
    output = ""
    ready_queue = []
    io_queue = []

    # While there are processes to schedule
    while any(not p.completed for p in processes):
        # Add processes that have arrived to the ready queue
        for process in processes:
            if process.arrival == time and not process.completed:
                ready_queue.append(process)

        # Handle I/O events
        if io_queue:
            io_process = io_queue.pop(0)
            output += f"!{io_process.name}"
            # Add the process back to the ready queue after I/O
            ready_queue.append(io_process)

        # Schedule the next process from the ready queue
        if ready_queue:
            current_process = ready_queue.pop(0)
            run_time = 1  # We run each process for 1 time unit
            output += current_process.name
            current_process.remaining_time -= run_time

            # Handle completion and I/O scheduling
            if current_process.remaining_time == 0:
                current_process.completed = True
            elif current_process.next_io_time and (current_process.runtime - current_process.remaining_time) % current_process.io_freq == 0:
                io_queue.append(current_process)
            else:
                ready_queue.append(current_process)

        # Increment time
        time += 1

    return output


def main():
    # Open the file for reading
    try:
        with open(args.data_file, "r") as file:
            data = file.read()
    except FileNotFoundError:
        return 1

    # Parse the data to create process objects
    processes = parse_input(data)

    # Call the scheduler to get the output string
    output = scheduler(processes)

    return output


if __name__ == "__main__":
    scheduler_out = main()
    print(scheduler_out)
