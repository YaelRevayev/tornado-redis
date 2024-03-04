import os
import constant


# List all files in a directory using scandir()
basepath = constant.SRC_DIR_NAME
with os.scandir(basepath) as entries:
    for entry in entries:
        with open(entry.name, "rb") as image:
            f = image.read()
            b = bytearray(f)
            print b[0]
        