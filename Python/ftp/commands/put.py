#coding:utf-8

from commands.Command import Command
from modules.color import error

class put(Command):
    def __init__(self, args, ftp, address, user):
        Command.__init__(self, args, ftp, address, user)

    def call(self):
        try:
            file = "{}/{}".format(self.ftp.pwd(), self.argv[1])
            self.ftp.storbinary('STR {}'.format(self.argv[1]), open(file, 'rb'))
        except :
            error("You may not have permission to upload")
