requirements = {
    'a' : ['f'],
    'b' : ['f'],
    'c' : ['d'],
    'd' : ['a', 'b'],
    'e' : [],
    'f' : []
}

installed = {
    'a' : False,
    'b' : False,
    'c' : False,
    'd' : False,
    'e' : False,
    'f' : False
}

installationOrder = []

def install(project):
    installed[project] = True

    for dependency in requirements[project]:
        if not installed[dependency]:
            install(dependency)

    installationOrder.append(project)

if __name__ == '__main__':
    for project in 'abcdef':
        if not installed[project]:
            install(project)

    print(installationOrder)