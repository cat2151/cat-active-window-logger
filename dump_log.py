import tomlkit

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
