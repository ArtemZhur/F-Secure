import argparse

import workerpool
import json
import multiprocessing as mp

from listener import Listener
from task import MyTask


workers = workerpool.WorkerPool(100)


def main():

    parser = argparse.ArgumentParser(description='Set configuration.')

    parser.add_argument("-c", "--file", type=str, nargs=1,
                        metavar=('file'), help="Choose file with URL's list")

    parser.add_argument("-l", "--log", type=str, nargs=1,
                        metavar=('log'), help="Choose log file")

    args = parser.parse_args()

    with open(args.file[0]) as file:
        data = json.load(file)
        dict_list = data['pages']

    manager = mp.Manager()
    q = manager.Queue()
    pool = mp.Pool(mp.cpu_count() + 2)
    listener = Listener(q, args.log[0])



    for web_page in dict_list:
        workers.put(MyTask(web_page, q))

    w = pool.apply_async(listener.listener())

if __name__ == "__main__":
   main()
