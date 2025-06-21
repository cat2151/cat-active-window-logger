import tomlkit

# TODO hardcodingになっているtoml filenameを、他のpy同様に、tomlとargsの仕組みを使って、tomlファイルで定義可能にする
#  実際には、tomlで、指定dirすべてのlog fileを対象とするよう指定、でまず運用して検証する想定

def main():
    toml = load_toml("active_window_log.toml")
    print_window_info(toml, "active_window_information")
    print_window_info(toml, "topmost_window_information")

def print_window_info(toml, info_name):
    print(f"Information from {info_name}:")
    for info in toml[info_name]:
        print(info)
    print()

def load_toml(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return tomlkit.load(file)

if __name__ == "__main__":
    main()
