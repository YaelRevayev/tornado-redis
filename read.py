import os
import constant


def read_files_from_dir(basepath = constant.SRC_DIR_NAME):
    dict = {}
    with os.scandir(basepath) as entries:
     for entry in entries:
            with open("{0}/{1}".format(basepath,entry.name), "rb") as image:
                 file = image.read()
                 dict[entry.name] = bytes(bytearray(file))

    return dict

        