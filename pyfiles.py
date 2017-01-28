import os
import time
from pandas import DataFrame


def lf(path='.', full=False):
    file_list = os.listdir(path)
    file_list = [os.path.join(path, f) for f in file_list] if full else file_list
    return file_list

def lf_size(path='.'):
    file_paths = lf(path, full=True)
    return [os.path.getsize(fp) for fp in file_paths]

def lf_type(path='.'):
    dir_content = lf(path, full=True)
    dir_list = [os.path.isdir(dc) for dc in dir_content]  
    types = ['dir' if d else 'file' for d in dir_list]
    return types

def lf_date(path='.'):
    epoch_time = [os.stat(f).st_mtime for f in lf(path, full=True)]
    fmt = '%Y-%m-%d %H:%M:%S'
    time_stamp = [time.strftime(fmt, time.gmtime(et)) for et in epoch_time]
    return time_stamp
    
def lf_all(path='.', as_df = True):
    dir_details = zip(lf(path), lf_type(path), lf_size(path), lf_date(path))
    if as_df:
        cols = ['name', 'type', 'bytes', 'modified']
        dir_details = DataFrame(dir_details, columns=cols)
    return dir_details