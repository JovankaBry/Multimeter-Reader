import time
import sys 
import select
from .serials import open_serial
from .csv import get_filename, file
from .func import query, resistance, voltage, get_key