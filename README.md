# 🚧 Check Point Firewall IP Blocker Script

This Python script automates the process of generating Check Point Firewall host addition commands for blocking a list of IP addresses. Users are prompted to input an incident number, date, PIC, and a list of IP addresses. The script formats the input data into a series of "add host" commands, which can then be executed in the Check Point Firewall environment to block the specified IP addresses.

## ✨ Features

- Prompt for user input (incident number, date, PIC, list of IP addresses)
- Generate formatted "add host" commands for Check Point Firewall
- Replace tabs with spaces in the final output

## 📋 Prerequisites 

- Python 3.x

## 🚀 Usage

1. Clone this repository or download the script.
2. Open a terminal and navigate to the directory where the script is located.
3. Run the script using `python3 ip_blocker.py` (or `python ip_blocker.py` if your default Python version is 3.x).
4. Follow the prompts to enter the incident number, date, PIC, and list of IP addresses.
5. The script will generate the formatted "add host" commands.
6. Copy the generated commands and execute them in the Check Point Firewall environment to block the specified IP addresses.

## 📄 License

[MIT](https://choosealicense.com/licenses/mit/)

