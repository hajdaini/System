#coding:utf-8

import importlib, pkgutil, inspect
from modules.color import *

class Loader:
    def is_package(self, component):
        try:
            component = importlib.import_module(package)
        except:
            return False
        return hasattr(component, "__path__")

    def list(self, package):
        modules = []
        try:
            package = importlib.import_module(package)
        except:
            return modules
        if hasattr(package, "__path__"):
            for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
                modules.append(modname)
        return modules

    def load(self, component, executable=None):
        if executable == None:
            executable = component.split(".")[-1]
        try:
            package = importlib.import_module(component)
        except:
            return None
        if hasattr(package, "__path__"):
            modules = {}
            for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
                executable = self.load_module("{}.{}".format(component, modname), modname)
                if executable == None:
                    return None
                modules[modname] = executable
            return modules
        else:
            return self.load_module(component, executable)

    def load_module(self, component, executable=None):
        try:
            module = importlib.import_module(component)
        except:
            return None
        if component.split(".")[-1][0].islower():
            if executable != None:
                try:
                    return getattr(module, executable)
                except:
                    return None
            else:
                return module
        if executable == None:
            executable = component.split(".")[-1]
        try:
            executable = getattr(component, executable)
        except:
            return None
        return executable() if inspect.isclass(executable) else executable
