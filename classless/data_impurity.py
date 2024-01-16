class Configuration:
    def __init__(self):
        self.config_data = {}

    def set_config(self, key, value):
        self.config_data[key] = value

    def get_config(self, key):
        return self.config_data.get(key)

# Example usage
config_instance = Configuration()
config_instance.set_config('username', 'user123')
config_instance.set_config('password', 'pass456')

username = config_instance.get_config('username')
password = config_instance.get_config('password')

print("Username:", username)
print("Password:", password)

