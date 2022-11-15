try:
    f=open("/home/guari/File/Message.py","r")
    print(f.read())
finally:
    f.close()