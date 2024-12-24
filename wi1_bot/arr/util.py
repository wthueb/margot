import logging
import pathlib

from wi1_bot.config import RemotePathMapping, config


def replace_remote_paths(path: pathlib.Path) -> pathlib.Path:
    if "general" not in config or "remote_path_mappings" not in config["general"]:
        return path

    mappings = config["general"]["remote_path_mappings"]

    most_specific: RemotePathMapping | None = None

    for mapping in mappings:
        if path.is_relative_to(mapping["remote"]):
            mapping_len = len(pathlib.Path(mapping["remote"]).parts)
            most_specific_len = (
                len(pathlib.Path(most_specific["remote"]).parts) if most_specific is not None else 0
            )

            if mapping_len > most_specific_len:
                most_specific = mapping

    if most_specific is not None:
        remote_path = path
        path = pathlib.Path(most_specific["local"]) / path.relative_to(most_specific["remote"])

        logging.getLogger(__name__).debug(f"replaced remote path mapping: {remote_path} -> {path}")

    return path
