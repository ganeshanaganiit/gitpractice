import configparser

config= configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class ReadConfig:
        @staticmethod
        def getapplicationurl():
                url=config.get('common info','baseurl' )
                return url
