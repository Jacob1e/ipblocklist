incident_number = input("Enter the incident number: ")
incident_date = input("Enter the date (e.g., 12/25/2023): ")
user_pic = input("Enter your PIC: ")

print("Enter the list of IP addresses (one per line, followed by a blank line to finish):")
ip_list_input = []
while True:
    line = input()
    if line:
        ip_list_input.append(line)
    else:
        break

ip_addresses = [ip.strip() for ip in ip_list_input]

formatted_output = ""

for ip in ip_addresses:
    line = f'add host name "Bad_Hst_{ip}" ip-address "{ip}" groups.5 "Exploits_2023" comments "INC{incident_number} {user_pic} {incident_date}"\n'
    line = line.replace('\t', ' ')
    formatted_output += line

print(formatted_output)

