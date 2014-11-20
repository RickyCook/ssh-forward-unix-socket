#!/usr/bin/env python

import argparse
import logging
import os

try:
    import shutil
    SOCAT_COMMAND = shutil.which('socat')
except AttributeError:
    import distutils.spawn
    SOCAT_COMMAND = distutils.spawn.find_executable('socat')

PARSER = argparse.ArgumentParser(description="Forward unix sockets over SSH")
PARSER.add_argument("--local_path", help="override the local path. If not given, mirrors the remote_path")
PARSER.add_argument("ssh_command", help="command to connect to the remote host. Example: ssh myuser@myhost")
PARSER.add_argument("remote_path", help="path to the remote socket to forward")

SOCAT_COMMAND = (SOCAT_COMMAND,
                 'UNIX-LISTEN:{local_path},reuseaddr,fork',
                 'EXEC:{ssh_command} socat STDIO UNIX-CONNECT\\:{remote_path}',
                 )

logging.basicConfig(level=logging.DEBUG)

def main():
    args = PARSER.parse_args()
    logging.debug(args)

    remote_path = args.remote_path
    local_path = args.local_path or remote_path
    real_socat_command = [
        s.format(
            local_path=local_path,
            remote_path=remote_path,
            ssh_command=args.ssh_command,
        )
        for s in SOCAT_COMMAND]
    logging.debug("Real socat command: %s", real_socat_command)

    logging.info("Spawning the socat process")
    os.execvp(real_socat_command[0], real_socat_command)

if __name__ == '__main__':
    main()
