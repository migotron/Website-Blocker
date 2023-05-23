# Website Blocker
This is a simple Python script that blocks access to specified websites during working hours by modifying the host file on your local machine. The script uses a list of websites to block and a redirect IP address to achieve this.

## Usage
### To use this script, follow these steps:
    1.) Open the script in your preferred text editor.
    2.) Modify the website_list list to include the websites you want to block.
    3.) Modify the hosts_path variable to point to the location of your host file.
    4.) Run the script using a Python interpreter.
    5.) The script will run indefinitely, checking the time every 5 seconds. 

If the current time is within working hours (9 AM to 5 PM), the script will add the specified websites to the host file, effectively blocking access to them. If the current time is outside working hours, the script will remove the specified websites from the host file, allowing access to them.

# Author
This script was created by **Miguel Ibarra**. If you have any questions or suggestions, you can contact me at my GitHub profile. 
【=◈︿◈=】
