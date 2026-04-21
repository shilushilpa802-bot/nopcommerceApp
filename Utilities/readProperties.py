import configparser
import os

# Create parser object
config = configparser.RawConfigParser()


# # Get current file directory
# current_dir = os.path.dirname(os.path.abspath(__file__))
#
# # Build path to config.ini
# config_path = os.path.join(current_dir, "..", "Configuration", "config.ini")
#
# # Read config file
# config.read(config_path)

# # Read config file
config.read("D:\\Shilpa\\Python\\PycharmProjects\\nopcommerceApp\\Configuration\\config.ini")


class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url=config.get('common info', 'baseURL')
        return url
    @staticmethod
    def getUseremail():
        username=config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password=config.get('common info', 'password')
        return password
