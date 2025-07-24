a = 10
b = 0
try:
    print(a/b)
    try:
        f = open('msg.txt', 'w')
        f.write("Hello this is text file")
        print("File is updated")
    except Exception as e:
        print(e)
except Exception as e:
        print(e)
