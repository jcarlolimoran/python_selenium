
def getloc(key):
    fileName = "E:/automation/MySelenium_New/files/file.txt"
    fileObj = open(fileName)

    # read file
    for line in fileObj:
        line = line.strip()
        if line.startswith(key) and not line.startswith("#"):
            keyvalue = line.split("|LOCATOR|")
            if keyvalue[0] == key:
                print(keyvalue[1])
                break
    return str(keyvalue[1])






