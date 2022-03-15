import getpass
import pipes

import tomli

try:
    with open(f"/usr/{getpass.getuser()}/pyproject.toml", "r") as f:
        toml_str = f.read()

    toml_dict = tomli.loads(toml_str)
    type_checker = toml_dict["tool"]["ty"]["type_checker"]
    print(f"export TY_TYPE_CHECKER={pipes.quote(type_checker)}")
except:
    print(f'export TY_TYPE_CHECKER=""')
