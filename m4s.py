import json
import requests
from pathlib import Path
from zipfile import ZipFile

def get_json(json_file: Path):
    data = json_file.read_text()
    return json.loads(data)

CONFIG = get_json(Path('config.json'))

def clear_dir(dir: Path):
    for child in dir.iterdir():
        if child.is_file():
            child.unlink()
        elif child.is_dir():
            clear_dir(child)
            child.rmdir()

def ready_dir(dir: Path):
    if dir.exists():
        clear_dir(dir)
    else:
        dir.mkdir()

def copy_file(src: Path, dest_dir: Path):
    (dest_dir / src.name).write_bytes(src.read_bytes())

def copy_dir(src_dir: Path, dest_dir: Path):
    ready_dir(dest_dir)
    for child in src_dir.iterdir():
        if child.is_file():
            copy_file(child, dest_dir)
        elif child.is_dir():
            copy_dir(child, dest_dir / child.name)

def install_mod(mod, install_dir: Path):
    r = requests.get(mod['url'])
    zip_file = Path(mod['name'] + '.zip')
    print('Downloading', mod['name'], 'zip...')
    zip_file.write_bytes(r.content)
    with ZipFile(str(zip_file), 'r') as zip_ref:
        print('Extracting', mod['name'], 'zip...')
        zip_ref.extractall(str(install_dir))
    zip_file.unlink()

def main():
    sims_dir = Path(CONFIG['simsdir'])
    if not sims_dir.exists():
        raise Exception('The Sims directory does not exist.')
    
    if CONFIG['backup']['enabled']:
        backup_dir = Path(CONFIG['backup']['dir'])
        if not backup_dir.exists():
            raise Exception('The backup directory does not exist.')
        for folder in CONFIG['backup']['folders']:
            copy_dir(sims_dir / folder, backup_dir / folder)

    install_dir = sims_dir / 'Mods'
    if not install_dir.exists():
        install_dir.mkdir()
    for mod in CONFIG['modlist']:
        if mod['enabled']:
            mod_dir = install_dir / mod['name']
            ready_dir(mod_dir)
            install_mod(mod, mod_dir)


if __name__ == '__main__':
    main()