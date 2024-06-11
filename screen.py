import modules as md
regions = [(0, 50, 800, 40)]
ss_img = ""


def screen(name=None):
    globals()['ss_img'] = md.screenshot(region=regions[0])
    ss_img.save(md.path.join('Images/', 'ping' + name + ".png"))


def capture(*args):

    if args[0][1] == 'part':
        screen(args[0][0])

    else:
        image = md.screenshot()
        image.save(md.path.join('Images/', 'ping' + args[0][0] + ".png"))


capture(md.argv[1:])
