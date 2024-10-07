def read_data(filename):
    try:
        with open(filename, "r") as file:
            inputdata = file.read()
            return inputdata
    except FileNotFoundError as filerror:
        print(filerror)
        return None
