from pathlib import Path
path=Path("testings")
print(path.exists())
#path.mkdir() # create a directory
#path.rmdir() #remove the directory
#path.rename("mytest")
paths=[p for p in path.iterdir() if p.is_dir()]
py_files=[p for p in path.rglob("*.py")]
print(py_files)
