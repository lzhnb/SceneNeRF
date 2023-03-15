# Copyright (c) Zhihao Liang. All rights reserved.
import os
import argparse

import torch
import omegaconf

import snerf


def get_args() -> argparse.Namespace:
    parser = snerf.get_default_args()
    parser.add_argument("--seed", type=int, default=123456, help="Random seed")

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    # read args and convert into config
    args = get_args()
    conf = snerf.merge_config_file(args)
    print("Config:\n", omegaconf.OmegaConf.to_yaml(conf))

    # init device in torch
    device = "cuda" if torch.cuda.is_available() else "cpu"

    # set random seed
    snerf.set_random_seed(conf.seed)
