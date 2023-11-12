"""Generate ./docs/DATA_STREAM.md
"""
from logging import DEBUG, basicConfig, getLogger
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader

basicConfig(level=DEBUG)
logger = getLogger(__name__)

TARGET_DATA_STREAM = [
    "atr-qags",
    "e4-acc",
    "e4-bvp",
    "e4-eda",
    "e4-temp",
    "kinect-2d-kpt",
    "kinect-3d-kpt",
    "kinect-depth2",
    "rs02-depth",
    "lidar-depth",
    "system-ht-original",
    "system-order-sheet",
    "system-printer",
]


def main():

    streams = []
    for stream_name in TARGET_DATA_STREAM:
        path = Path(f"../../configs/dataset/stream/{stream_name}.yaml")
        logger.info(f"load DataStreamConfig from {path}")
        with open(path, "r") as f:
            data = yaml.safe_load(f)
        streams.append(data)

    # build python script with jinja2
    env = Environment(
        loader=FileSystemLoader("./templates"),
        trim_blocks=True
    )

    template = env.get_template("DATA_STREAM.md.jinja")
    code = template.render(streams=streams)

    # write a python script
    path = Path("../../docs/DATA_STREAM.md")
    logger.info(f"write docs/DATA_STREAM.md to {path}")
    with open(path, "w") as f:
        f.write(code)


if __name__ == "__main__":
    main()