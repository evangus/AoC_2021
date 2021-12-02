def read_input(filename, split_lines = True, convert_to_int = True):
    f = open(filename)
    raw = f.read()[:-1]
    f.close()
    data = raw
    if split_lines:
        data = data.split('\n')
    if convert_to_int:
        data = [int(item) for item in data]
    return data