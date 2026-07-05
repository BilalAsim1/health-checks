import shutil

def check_disk_usage(disk, min_percent):
    """Return True if there's enough free disk space."""
    du = shutil.disk_usage(disk)
    percent_free = 100 * du.free / du.total
    return percent_free >= min_percent

def main():
    if check_disk_usage("/", 20):
        print("Everything OK - enough disk space")
    else:
        print("WARNING - low disk space")

if __name__ == "__main__":
    main()