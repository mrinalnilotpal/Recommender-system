# To be continued 

import numpy as np
import pandas as pd
import json, glob
import requests
import re
import tmdb
from importlib import reload
from utils import create_directory, update_progress

links = pd.read_csv("links.csv", dtype={"tmdb_id": 'Int64' })


links.shapesample_id = links.tmdb_id[0]
tmdb.movie(sample_id)
