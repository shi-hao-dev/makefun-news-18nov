# A news-image-daily entry (Python 3.13, standard library only): its image is the
# entry.png beside this file, and the program copies it to /output/entry.png. The
# image sums up Wednesday 18 November 2026's world news: Xi and Putin's meeting
# in Shenzhen, Iran's strikes on Kuwait and Bahrain, the Kerch Bridge hit for a
# second day, Mary Peltola's Alaska Senate win, Nvidia's board saying no to
# Jensen Huang's return, and Cyclone Akvan bearing down on Odisha. It is drawn
# once, from the day's reporting, and copied unchanged, so two runs write the
# same bytes.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "entry.png", OUT / "entry.png")
