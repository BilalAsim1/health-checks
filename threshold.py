import shutil

# Minimum free disk space required
THRESHOLD = 20

def check_disk(disk):
    du = shutil.disk_usage(disk)
    percent_free = 100 * du.free / du.total
    return percent_free >= THRESHOLD

if __name__ == "__main__":
    if check_disk("/"):
        print("Disk OK")
    else:
        print("Disk LOW")
        