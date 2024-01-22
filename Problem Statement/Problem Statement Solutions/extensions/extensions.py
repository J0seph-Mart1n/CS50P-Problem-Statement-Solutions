file = input("File name: ").lower().strip()
if ".gif" in file:
    print("image/gif")
elif file[-5:]=='.jpeg':
    print("image/jpeg")
elif file[-4:] == '.jpg':
    print("image/jpeg")
elif ".png" in file:
    print("image/png")
elif ".pdf" in file:
    print("application/pdf")
elif ".txt" in file:
    print("text/plain")
elif ".zip" in file:
    print("application/zip")
else:
    print("application/octet-stream")
