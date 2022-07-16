SERVER = "create-server"
SSERVER = "set-server"
CONNECTION = "create-connection"
PING = "ping"
CONFIG = "ip-config"
TRACE = "traceroute"
TRACER = "tracert"
DISPLAY = "display-servers"


# Creates the servers with the information passed through
def create_server(server_name, ip_address, server):

    if (server_name or ip_address) in server:  # Checks if server or ip is already i internet
        print("Server already created: Try again.")
        print()

    else:

        if validate_ip_address(ip_address):  # Validates ip
            server[server_name] = {"address": ip_address, "connection": {}}
            print("Success: A server with name", server_name, "was created at ip", ip_address, ".")
            print()

        else:
            print("Invalid ip address, cannot be added to server.")
            print()


# Creates a connection between servers
def create_connection(server_name_1, server_name_2, time, server):

    if (server_name_1 and server_name_2) in server:  # Checks if both servers are in my internet

        if server_name_2 in server[server_name_1]["connection"]:  # Checks if servers are already connected
            print("Servers are already connected.")
            print()

        else:  # Connects servers
            server[server_name_1]["connection"][server_name_2] = time
            server[server_name_2]["connection"][server_name_1] = time
            print("Success: A server with name", server_name_1, "is now connected to", server_name_2, ".")
            print()

    else:
        print("One or the other server not found please enter an existing server.")
        print()


# Sets the starting position of our internet connections
def set_server(setter, server):

    if setter in server:  # checks if that server is in the internet
        print("Server", setter, "selected.")
        print()
        return setter

    else:
        print("Server not found, enter a valid server.")
        print()


# Checks if the passed in parameter is an ip_address or server name
def ip_checker(address):

    ip = True
    asc_vals = [46, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57]
    for i in address:
        if ord(i) not in asc_vals:
            ip = False

    return ip


# Converts ips to server names
def ip_convert(address, server):
    final = address
    for num in server:
        if address == server[num]["address"]:
            final = num

    return final


def ping(internet, starting_place, destination, visit, times):

    if destination == starting_place:
        return times

    else:
        for node in visit:
            if starting_place == node:
                return None

        visit.append(starting_place)
        if ip_checker(destination):
            use = ip_convert(destination, internet)
            for node in internet[starting_place]["connection"]:

                if node not in visit:
                    path = ping(internet, node, use, visit, times)

                    if not path:
                        times += int(path)
                        return times + int(internet[starting_place]["connection"][node])
        else:
            for node in internet[starting_place]["connection"]:

                if node not in visit:
                    path = ping(internet, node, destination, visit, times)

                    if not path:
                        times += int(path)
                        return times + int(internet[starting_place]["connection"][node])


# Traces the path to the destination
def traceroute(internet, starting_place, destination, visit):
    if destination == starting_place:
        return visit

    visit.append(starting_place)

    for node in internet[starting_place]["connection"]:
        if ip_checker(destination):
            use = ip_convert(destination, internet)
            if node not in visit:
                path = traceroute(internet, node, use, visit)
                if path:
                    print("Trace Complete")
                    return path
        else:
            if node not in visit:
                visit.append(node)
                path = traceroute(internet, node, destination, visit)
                if path:
                    print("Trace Complete")
                    return path


# Gets the current server location
def ip_config(spot, server):

    if spot != "":  # Checks if a server has been set to the starting point
        print(spot, server[spot]["address"])
        print()
    else:
        print("No starting position has been set.")
        print()


# Displays all the servers
def display_server(server):

    for node in server:  # Iterates through the different servers in my internet
        print(node, server[node]["address"])

        if server[node]["connection"] == {}:  # Checks if a connection is empty
            print("No connections found")
            print()

        else:
            for x in server[node]["connection"]:
                print("\t", x, server[x]["address"], server[node]["connection"][x])


# Validates the ip address given
def validate_ip_address(address):
    sections = address.split(".")
    check = 0

    for part in sections:  # Iterates through the parts of an ip address
        if type(int(part)) != type(check):
            return False

        if int(part) < 0 or int(part) > 255:
            return False

    return True


# Driver Code
def main():
    server = {}
    visited = []
    start = ""
    time = 0

    com = input(">>> ").lower().split()

    while com[0] != "quit":

        if com[0] == SERVER:
            create_server(com[1], com[2], server)

        elif com[0] == DISPLAY:
            display_server(server)

        elif com[0] == CONNECTION:
            create_connection(com[1], com[2], com[3], server)

        elif com[0] == SSERVER:
            start = set_server(com[1], server)

        elif com[0] == CONFIG:
            ip_config(start, server)

        elif com[0] == PING:
            time = ping(server, start, com[1], visited, time)
            if time is None:
                time = 0
            print("Reply from", com[1], "time =", time, "ms")
            print()

        elif com[0] == TRACE or com[0] == TRACER:
            print("Tracing route to", com[1])
            print(traceroute(server, start, com[1], visited))

        com = input(">>> ").split()


if __name__ == "__main__":
    main()
