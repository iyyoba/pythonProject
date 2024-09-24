# Exercise 3
dashboard = {}
def askingInfo():
    print("Choose what you want to do:")
    print("n: add new airport")
    print("f: fetch airport name")
    print("ENTER to quit program")
    return input()

query = askingInfo()
while query == "n" or query == "f":
    if query == "n":
        newIcao = input("input ICAO code: ")
        newName = input("input name of airport: ")
        dashboard.update({newIcao: newName})
    else:
        icao = input("input ICAO code: ")
        if icao in dashboard:
            print("Airport name:", dashboard[icao])
        else:
            print("Airport not found")
    query = askingInfo()
print("Thank you! Bye!")