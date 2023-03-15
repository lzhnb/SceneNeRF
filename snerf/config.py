# Copyright (c) Zhihao Liang. All rights reserved.
import argparse

from omegaconf import OmegaConf


def get_default_args() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()

    # necessary path
    group = parser.add_argument_group("essential path")
    group.add_argument(
        "--config",
        "-c",
        type=str,
        default=None,
        help="Config yaml file (will override args)",
    )

    return parser


def merge_config_file(args: argparse.Namespace) -> OmegaConf:
    """
    Load json config file if specified and merge the arguments
    """
    args_conf = OmegaConf.create(vars(args))
    yaml_conf = OmegaConf.load(args.config)
    conf = OmegaConf.merge(args_conf, yaml_conf)
    return conf
