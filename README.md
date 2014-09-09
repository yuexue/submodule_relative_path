# submodule\_relative\_path

A python script for changing git submodule's path to relative path w.r.t the super repo.

The script will help you aboutt:

- Move git repo directory with submobule to some other location.
- Share a git repo with submodule via samba.
- Share a git repo with submodule via docker volume mapping.

The script do two things:

- Change __gitdir__ location in .git file of each submodule.
- Change config of each submodule in .git/modules/ .

## Usage

First, copy the submodule\_relative\_path.py to the directory of superrepo.

Second, run the script.

    ./submodule_relative_path.py

