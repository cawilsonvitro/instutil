import os
import toml


def update_pck(pck_name:str, api_token:str) -> None:
    """_summary_ this removes previous build, updates current built and version in project .toml, file struct should be as below\n
    folder\n
        |_src\n
        |__code\n
        |_dist\n
        |_pyproject.toml\n
        |_pkgworkflow.py
        |_script to call pkgworkflow

    Args:
        api_token (str): token for the api DO NOT UPLOAD PUBLICLY IMPORT TO PYTHON SCRIPT EXERTNALLY AND EXECUTE THERE
        pck_name (str): name of src folder
    """
    #check for dist folder, and source foulder
    cwd = os.getcwd()
    # src_path = f"{cwd}\\{pck_name}"
    dist_path = f"{cwd}\\dist"
    # pyproject_path = f"{cwd}\\pyproject.toml"
    
    
    # version:int = 0 
    
    
    #clearing dist path 
    for dirpath,_,files in os.walk(dist_path):
        for file in files:
            os.remove(f"{dirpath}\\{file}")
        
    #updating verson number
    
    tomlpath = "pyproject.toml"
    
    with open(tomlpath, "r") as f:
        metadata = toml.load(f)
    vers:list[str] = metadata['project']["version"].split(".")
    i:int = 0
    for ver in vers:
        vers[-(i+1)] = str(int(vers[-(i+1)]) + 1)
        if int(vers[-(i+1)]) < 10: #if our version is < 10
            break
        else:
            vers[-(i+1)] = '0'
        i += 1
    version:str = (".").join(vers)
    
    
    metadata['project']["version"] = version
    
    with open(tomlpath, '+w') as f:
        toml.dump(metadata, f)
    
    #build wheel files
    os.system("python -m build")
    
    
    #upload to pypi
    
    os.system(f"twine upload --repository pypi dist/* -u __token__ -p {api_token}")
    
if __name__ == "__main__":
    api_token = 'NO'
    update_pck('instutil', api_token)
    