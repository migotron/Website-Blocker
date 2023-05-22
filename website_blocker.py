import time
from datetime import datetime as dt

# Location of the host file
hosts_path = "/etc/hosts"

# IP address to redirect blocked websites to
redirect = "127.0.0.1"

# List of websites to block
website_list = ["www.facebook.com", "facebook.com", "www.twitter.com", "twitter.com"]

# Loop indefinitely
while True:
    # Check if the current time is within working hours (9 AM to 5 PM)
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        print("Working hours...")

        # Open the host file in read/write mode
        with open(hosts_path, "r+") as file:
            content = file.read()

            # For each website in the list of websites to block
            for website in website_list:
                # Check if the website is already present in the host file
                if website in content:
                    pass
                else:
                    # If the website is not present, add it to the host file with the redirect IP address
                    file.write(redirect + " " + website + "\n")
    else:
        # If it is not within working hours, remove the blocked websites from the host file
        with open(hosts_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun hours...")

    # Sleep for 5 seconds before checking the time again
    time.sleep(5)
