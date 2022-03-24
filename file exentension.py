fn = input("enter filename: ")
ext = fn.split(".")
print("this file is a : " + repr(ext[-1]) + "file")
