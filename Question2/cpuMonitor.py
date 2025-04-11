import psutil    #importing the libraries
#=========================================================================================
# This function monitors the CPU usage of the system and prints it to the console.
# It uses the psutil library to get the CPU usage percentage.
#*************************************************************************************
# to run the program uninterruptedly, 
# use the command: 
#   1. nohup python cpuMonitor.py &
#   2. can create a cron job to run this script at regular intervals.
#   3. can use systemd service to run this script as a background service.
#=========================================================================================== 

def get_cpu_usage():
    """
    Get the current CPU usage percentage.
    """
    print("Monitoring CPU usage...")
    # Get the CPU usage percentage
    return psutil.cpu_percent(interval=1)  # interval specifies how long to wait (in seconds)

'''Main function to execute the script'''
if __name__ == "__main__":
    try:
        print("Starting CPU usage monitoring...")
        cpu_usage = get_cpu_usage()      #call the function to get CPU usage
    except Exception as e:
        print(f"An error occurred while capturing the cpu details : {e}")
        print("Exiting...")              # Exit the script with a non-zero status code to indicate failure
        exit(1)
    
    # Check if CPU usage exceeds 80%
    if cpu_usage>=80:
        print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")
    else:
        print(f"CPU usage is normal: {cpu_usage}%")
    
