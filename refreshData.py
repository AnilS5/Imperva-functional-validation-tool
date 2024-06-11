"""
    This function reset the values against keys in data.yaml to default None.

    Libraries:
     - yaml

    Parameters:
     - None

    Usage:
     refreshData()
"""

# Libraries
import modules as md
from readYaml import readYaml
from writeYaml import writeYaml
from yamlData import yamlData


def update_data(*args):
    data = readYaml('data.yaml')
    keys = yamlData()
    if args[0] in keys:
        for k in range(len(keys[args[0]])):
            data[keys[args[0]][k]] = args[1][k]

    else:
        for key, value in keys.items():
            for k in value:
                data[k] = ' '

    writeYaml(data)

