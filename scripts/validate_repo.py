"""Check portable paths, local Markdown links, and optional ZIP byte parity."""
from pathlib import Path, PurePosixPath
import argparse
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ['SKILL.md', 'INSTALL.md', 'agents/openai.yaml',
            'references/formats.md', 'references/project-records.md', 'references/quality.md']

def validate(archive=None):
    for relative in REQUIRED:
        assert (ROOT / relative).is_file(), f'Missing {relative}'
    skill = (ROOT / 'SKILL.md').read_text(encoding='utf-8-sig')
    header = re.match(r'\A---\n(.*?)\n---\n', skill, re.S)
    assert header, 'Missing frontmatter'
    assert re.search(r'^name: art-skill$', header[1], re.M), 'Incorrect skill name'
    assert re.search(r'^description: \S', header[1], re.M), 'Missing description'
    checked = 0
    for file in ROOT.rglob('*.md'):
        if '.git' in file.parts:
            continue
        content = file.read_text(encoding='utf-8-sig')
        for link in re.findall(r'\]\(([^)]+)\)', content):
            if re.match(r'^(?:https?://|mailto:|#)', link):
                continue
            target = (file.parent / link.split('#', 1)[0]).resolve()
            assert target.is_relative_to(ROOT), f'Nonportable link in {file.name}: {link}'
            assert target.exists(), f'Broken link in {file.name}: {link}'
            checked += 1
    if archive:
        with zipfile.ZipFile(archive) as package:
            assert package.testzip() is None, 'ZIP integrity failure'
            names = package.namelist()
            for name in names:
                path = PurePosixPath(name)
                assert path.parts[0] == 'art-skill' and '..' not in path.parts, f'Unsafe ZIP path: {name}'
                assert not path.is_absolute(), f'Absolute ZIP path: {name}'
                local = ROOT.joinpath(*path.parts[1:])
                assert local.is_file() and package.read(name) == local.read_bytes(), f'Byte mismatch: {name}'
            for relative in REQUIRED:
                assert 'art-skill/' + relative in names, f'ZIP missing {relative}'
            assert not any('/examples/' in name or '/.git/' in name for name in names), 'Non-runtime content in ZIP'
    print(f'PASS: required files, frontmatter, {checked} local links' + (', ZIP integrity/path checks/byte parity' if archive else ''))
    print('These checks do not establish image quality, model behavior, or audience performance.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--zip')
    validate(parser.parse_args().zip)
