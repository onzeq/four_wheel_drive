import scripts.drive.drives as drives

def main():
    motors = drives.get_motors()
    drives.stop(motors)


if __name__ == '__main__':
    main()