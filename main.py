import os
import shutil
import argparse
import time

def log(string, logs):
    print(string)
    with open(logs, 'a') as f:
        f.write(string + '\n')

def copy(source, destination, logs):
    try:
        log('From: ' + source + ' to: ' + destination, logs)
        shutil.copy(source, destination)
    except:
        log('This file exists', logs)

def files(source, destination, logs):
    for folder, subfolders, filenames in os.walk(source):
        log('The current folder is ' + folder, logs)
        for subfolder in subfolders:
            log('The current subfolder of ' + folder + ' is ' + subfolder, logs)
            try:
                new = folder.replace(source, destination)
                os.mkdir(new + '\\' + subfolder)
            except:
                log('This folder exists: ' + subfolder, logs)
        for filename in filenames:
            new = folder.replace(source, destination)
            file = folder + '\\' + filename
            copy(file, new, logs)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Folder synchronization tool")
    parser.add_argument("source_folder", help="Path to the source folder")
    parser.add_argument("replica_folder", help="Path to the replica folder")
    parser.add_argument("sync_interval", type=int, help="Sync interval in seconds")
    parser.add_argument("log_file", help="Path to the log file")

    args = parser.parse_args()
    while True:
        files(args.source_folder, args.replica_folder, args.log_file)
        time.sleep(args.sync_interval)
