#!/usr/bin/env python

import json
import pathlib
import sys
from zipfile import ZipFile


archive_name = sys.argv[1]
base_path = pathlib.Path(sys.argv[2])


def extract_object(path, container, archive, level=0):
    if container['object'] == 'container':
        path.mkdir()
        if level:
            title = f"{'#' * level} {container['title']}\n\n"
        else:
            title = f"% {container['title']}\n\n"
        extract_file(path / f"0-{container['slug']}.md", title.encode() + archive.read(container['introduction']))
        #extract_file(path / 'x-conclusion.md', archive.read(container['conclusion']))
        for i, child in enumerate(container['children'], 1):
            p = path / f"{i}-{child['slug']}"
            extract_object(p, child, archive, level+1)


def extract_file(path, content):
    path.write_bytes(content)


with ZipFile(archive_name, 'r') as archive:
    manifest = json.loads(archive.read('manifest.json'))
    extract_object(base_path, manifest, archive)
