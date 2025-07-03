from pathlib import Path
path=Path("testing/test.py")
print(path.exists())
print(path.is_file())
print(path.is_dir())
print(path.name)
print(path.stem) # with out extension
print(path.suffix)
print(path.parent)
path=path.with_suffix(".py")
print(path)
print(path.exists())