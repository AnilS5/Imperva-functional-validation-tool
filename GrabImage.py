import modules as md
def grabImage(*args):

    md.system("start /MAX /wait cmd /k ping {0} -n 2 ^& python screen.py {1} {2} ^& taskkill /f /im cmd.exe".format(args[0], args[1], args[2]))
    if len(args) == 4:
        #new_arg = args[3].replace('.', '-')
        new_arg = args[3]
        md.system("start /MAX /wait cmd /k ping {0} -n 2 ^& python screen.py {1} {2} ^& taskkill /f /im cmd.exe".format(args[3], new_arg, args[2]))
