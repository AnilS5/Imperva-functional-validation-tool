import modules as md

def virtualIP(*args):
    data = md.readYaml('data.yaml')
    data['initial_vip_check'] = args[0]
    md.writeYaml(data)

