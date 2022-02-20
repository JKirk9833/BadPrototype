import os
import pathlib
from helpers.managers.ConfigManager import ConfigManager
import tools.isotool as iso
import tools.bectool as bec


def setup_environment(iso_path, handle_progress):
    path = pathlib.Path(iso_path)
    output_dir = f"{path.parent}/{path.stem}"
    vanilla_dir = f"{output_dir}_VANILLA/"
    modded_dir = f"{output_dir}_MODDED/"
    ConfigManager().setup(f"{path.parent}")

    if not os.path.isdir(vanilla_dir):
        extract_all(path, vanilla_dir, handle_progress)
    if not os.path.isdir(modded_dir):
        extract_all(path, modded_dir, handle_progress)


def extract_all(path, custom_dir, handle_progress):
    iso.diagnose(
        f"{path}",
        custom_dir,
        f"{path.stem}_FileList.txt",
        False,
        handle_progress,
    )
    bec.diagnose(
        f"{custom_dir}gladius.bec",
        f"{custom_dir}/gladius_bec/",
        "bec_FileList.txt",
        False,
        handle_progress,
    )
