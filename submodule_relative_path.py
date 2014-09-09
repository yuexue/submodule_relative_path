#!/usr/bin/env python
'''
Change local git submodules path to relative path.
Usage:

    # Copy this file to the directory of superrepo,
    # and run it (make sure you have write permission
    # in every sub directories)
    ./submodule_relative_path.py
'''
import os
import re
import sys


def get_current_path():
    return os.path.abspath('.')


def get_modules():
    '''
    Get submodule list from .gitmodules file.
    '''
    path = '%s/.gitmodules' % get_current_path()
    if not os.path.exists(path):
        print("No .gitmodules file found.")
        return []
    else:
        content = open(path).read()
        modules = re.findall(r'\[submodule\s+?"(.+)?"\s*?\]\s+?path\s=\s([^\s]+)\s*?',
                             content, re.M)
        return modules


def convert_path(path):
    '''
    Convert path like abc/def to ../..
    '''
    return '/'.join(['..' for i in path.split('/') if i])


def replace_with_relative_path(module, path):
    '''
    Replace module 
    '''
    git_file = '%s/%s/.git' % (get_current_path(), path)
    if not os.path.exists(path):
        print("Error %s not exists." % path)
        return
    print("Patching %s ." % git_file)
    content = open(git_file).read()
    new_content = re.sub(r'gitdir:\s+?(.+?)/\.git',
                         'gitdir: %s/.git' % convert_path(path),
                         content)

    open(git_file, 'w').write(new_content)

    module_path = re.search(r"(\.git/.+)\s?", new_content).group(1)
    module_config = '%s/config' % module_path
    if not os.path.exists(path):
        print("Error %s not exists." % module_config)
        return
    print("Patching %s ." % module_config)
    module_content = open(module_config).read()
    new_module_content = re.sub(r"worktree\s*?=\s*?(.+)\s",
        "worktree = %s/%s\n" % (convert_path(module_path), path),
        module_content)
    open(module_config, 'w').write(new_module_content)


def main():
    modules = get_modules()
    for module, path in modules:
        replace_with_relative_path(module, path)


if __name__ == '__main__':
    main()
