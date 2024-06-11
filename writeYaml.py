import modules as md


def writeYaml(data):
    with open('data.yaml', 'w') as file:
        md.dump(data, file)
