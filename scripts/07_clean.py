from pathlib import Path
import shutil

# delete data subfolders + contents
if Path("../data/raw").exists():
    shutil.rmtree(Path("../data/raw"))
    
if Path("../data/processed").exists():
    shutil.rmtree(Path("../data/processed"))

# delete outputs folder + contents
if Path("../outputs").exists():
    shutil.rmtree(Path("../outputs"))
