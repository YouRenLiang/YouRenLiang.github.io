import configparser

def load_charsets(config_file='Config.ini'):
    config = configparser.ConfigParser()
    config.read(config_file, encoding='utf-8')
    char_set = config.get("BaseCharset", "CharSet")
    d62 = config.get("BaseCharset", "D62")
    return char_set, d62
