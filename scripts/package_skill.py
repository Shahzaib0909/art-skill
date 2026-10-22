"""Build a portable skill ZIP with Python's standard library."""
from pathlib import Path
import argparse
import zipfile

ROOT = Path(__file__).resolve().parents[1]

def build(output):
    files = [ROOT / 'SKILL.md', ROOT / 'INSTALL.md']
    files += sorted((ROOT / 'agents').rglob('*'))
    files += sorted((ROOT / 'references').rglob('*'))
    if (ROOT / 'LICENSE').is_file():
        files.append(ROOT / 'LICENSE')
    output = Path(output).resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
        for file in files:
            if file.is_file():
                archive.write(file, 'art-skill/' + file.relative_to(ROOT).as_posix())
    print(output)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', default=str(ROOT.parent / 'dist' / 'art-skill-v1.0.0.zip'))
    build(parser.parse_args().output)
