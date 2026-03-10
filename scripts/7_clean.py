from pathlib import Path
import shutil

# delete data subfolders + contents
if Path("../data/raw").exists():
    shutil.rmtree(Path("../data/raw"))
    
if Path("../data/processed").exists():
    shutil.rmtree(Path("../data/processed"))

if Path("../data/splits").exists():
    shutil.rmtree(Path("../data/splits"))

# delete artifacts folder + contents
if Path("../artifacts").exists():
    shutil.rmtree(Path("../artifacts"))

# delete predictions folder + contents
if Path("../predictions").exists():
    shutil.rmtree(Path("../predictions"))