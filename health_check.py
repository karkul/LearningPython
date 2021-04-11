from network import *
import shutil
import psutil


def check_disk_usage(disk):
    """ Verifies that there's enough free space on disk """
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
def check_cpu_usage():
    """Verifies that there's enough unused CPU"""
    usage = psutil.cpu_perccent(1)
    return usage < 75
# If there's not enough disk, or not enough CPU, print an error
if not check_cpu_usage('/') or not check_cpu_usage():
    print("Error!")
elif check_localhost() and check_connectiviy():
    print("Everything OK")
else:
    print("Network checks failed")


