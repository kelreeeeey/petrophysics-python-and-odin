# -*- coding: utf-8 -*-
"""
-----------------------------------------------------------
File: convert_jupyter_to_marimo.py
Author: Kelrey, T.
Email: taufiqkelrey1@gmail.com
Github: kelreeeeey
Description: convert jupyter notebooks from a subdir to
marimo notebooks in another subdir 
-----------------------------------------------------------
"""

from subprocess import run
from pathlib import Path

SOURCE_DIR = Path("./jupyter-notebooks/").resolve()
TARGET_DIR = Path("./marimo-notebooks/").resolve()

def make_comand_args(nb_src, nb_target) -> list[str]:
    return ["marimo", "convert", nb_src, "-o", nb_target]

def main() -> None:
    nbs = list(x for x in SOURCE_DIR.iterdir() if x.name.endswith(".ipynb"))
    for nb in nbs:
        nb_name = TARGET_DIR / (
            nb.name
            .replace(' - ', '_')
            .replace(' ', '_')
            .lower()
            .replace('.ipynb', '.py')
        )
        cmd_args = make_comand_args(nb_src=str(nb),
                                    nb_target=str(nb_name))
        print(f"Converting: {nb_name.name:<30}")
        run(cmd_args)
    return None

if __name__ == "__main__":
    main()
