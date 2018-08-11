#coding:utf-8

from pathlib import Path

def abspath(pwd, path):
    """
    Recompose un chemin absolu a partir de deux chaines quelconques
    """
    if path[0] == "/":
        return path
    pwd = pwd.split("/")
    del pwd[0]
    cpath = path.split("/")
    for idx, el in enumerate(path.split("/")):
        if el == ".." or el == ".":
            del cpath[0]
            if el == ".." and len(pwd):
                pwd.pop()
        else:
            break
    if (len(pwd)):
        pwd[0] = "/{}".format(pwd[0])
    return "{}/{}".format("/".join(pwd), "/".join(cpath))

def cabspath(path):
    """
    Recompose un chemin absolu a partir de la position sur le terminal client
    """
    if path[0] == "~":
        return str(Path.home()) + path[1:]
    try:
        pwd = str(Path.home())
        return abspath(pwd, path)
    except:
        return None

def sabspath(ftp, path):
    """
    Recompose un chemin absolu a partir de la position sur le yrtminal serveur
    """
    if path[0] == "~":
        return ftp.home + path[1:]
    try:
        pwd = ftp.pwd()
        return abspath(pwd, path)
    except:
        return None
