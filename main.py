import importlib.util
import sys


spec = importlib.util.spec_from_file_location("GUI", "./GUI/GUI.py")
GUI = importlib.util.module_from_spec(spec)
sys.modules["GUI"] = GUI
spec.loader.exec_module(GUI)


if __name__ == "__main__":
    pass
