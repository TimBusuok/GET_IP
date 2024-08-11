from pyfiglet import figlet_format
import socket
import sys



print("  ____ _____ _____   ___ ____")
print(" / ___| ____|_   _| |_ _|  _ \ ")
print("| |  _|  _|   | |    | || |_) |")
print("| |_| | |___  | |    | ||  __/")
print(" \____|_____| |_|   |___|_| ")

print("If you want help then write help")

while(True):
    ans = str(input("Enter your HOSTNAME(Example:<URL>.(com,ru and etc)): "))
    if ans != "help" or "exit":
        def get_id(target_host):
            try:
                ip = socket.gethostbyname(target_host)
                return ip
            except:
                print("Invalid IP\nPlease check your Hostname!!")

        if __name__ == "__main__":
            if ans == "exit":
                print("Goodbye!")
                sys.exit()
            elif ans == "help":
                print("Function in developing")
            else:
                read_host = ans
                IP = get_id(read_host)
                print("{} ==> {}".format(read_host, IP))
    else:
        if ans == "help":
            print("if you want exit them write in console - exit\nFunction in development")
