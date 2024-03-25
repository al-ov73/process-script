import argparse
import subprocess
import datetime


def create_process(process_name, filepath, restart, timer):
    timer = float(timer)
    if restart == 'true':
        start_time = datetime.datetime.now()
        with open(filepath, 'w') as f:
            process = subprocess.run(process_name, stdout=f, text=True)
        while True:
            diff = (datetime.datetime.now() - start_time).total_seconds()
            if diff > timer:
                break
            if process.returncode != 0:
                create_process(process_name, filepath, restart, timer)
    else:
        with open(filepath, 'w') as f:
            subprocess.run(process_name, stdout=f, text=True)


def main():
    parser = argparse.ArgumentParser(
        description='Create process'
    )
    parser.add_argument(
        'process_name', type=str, help='Process path'
    )
    parser.add_argument(
        'filepath', type=str, help='Filepath to save process output'
    )
    parser.add_argument(
        '--restart', type=str, help='Restart process in case of process fault',
        default='false', choices=['false', 'true']
    )
    parser.add_argument(
        '--timer', type=str, help='Timeout in seconds', default='false'
    )
    args = parser.parse_args()
    create_process(args.process_name, args.filepath, args.restart, args.timer)


if __name__ == '__main__':
    main()
