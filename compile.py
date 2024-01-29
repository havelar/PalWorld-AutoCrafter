import os, shutil

if __name__ == "__main__":
    os.system("pyinstaller --onefile autoCrafter.py")

    if os.path.exists("autoCrafter.exe"): os.remove("autoCrafter.exe")

    os.rename("./dist/autoCrafter.exe", "autoCrafter.exe")
    os.remove("autoCrafter.spec")
    shutil.rmtree("dist")
    shutil.rmtree("build")