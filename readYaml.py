import modules as md


def readYaml(data_file):
    with open(data_file, 'r') as file:
        data = md.load(file, Loader=md.FullLoader)
        return data
