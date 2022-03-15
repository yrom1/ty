import tomli

with open('pyproject.toml', 'r') as f:
    toml_str = f.read()

toml_dict = tomli.loads(toml_str)
type_checker = toml_dict['tool']['ty']['type_checker']
# print(type_checker)
