import importlib

def explore_attributes():
    mod_name = input("Enter module name to explore: ")
    try:
        module = importlib.import_module(mod_name)
        attrs = dir(module)
        print(f"Available Attributes in {mod_name} module:")
        print(attrs[:15])
    except ModuleNotFoundError:
        print("Module not found.")