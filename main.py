import read
import save
import constant

def main():
    dict_files_names_and_their_content = read.read_files_from_dir(constant.SRC_DIR_NAME)
    save.save_key_value_pair(dict_files_names_and_their_content)

if __name__ == "__main__":
    main()