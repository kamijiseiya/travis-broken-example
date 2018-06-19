import os
for k, v in os.environ.items():
    print("{key} : {value}".format(key=k, value=v))