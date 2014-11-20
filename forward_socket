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
PARSER.add_argument("--local_user", help="try to set the user the local socket is owned by")
PARSER.add_argument("--local_group", help="try to set the group the local socket is owned by")
PARSER.add_argument("--local_mode", help="try to set the file mode of the local socket")
PARSER.add_argument("ssh_command", help="command to connect to the remote host. Example: ssh myuser@myhost")
PARSER.add_argument("remote_path", help="path to the remote socket to forward")


logging.basicConfig(level=logging.DEBUG)

def main():
    args = PARSER.parse_args()
    logging.debug(args)

    socat_local_opts = []
    for opt_name in ('user', 'group', 'mode'):
        opt_val = getattr(args, 'local_%s' % opt_name)
        if opt_val:
            socat_local_opts.append('%s=%s' % (opt_name, opt_val))

    socat_local_opts_suffix = ''.join((
        ',%s' % opt_string for opt_string in socat_local_opts
    ))

    real_socat_command = (SOCAT_COMMAND,
                         'UNIX-LISTEN:{local_path},reuseaddr,fork%s' % socat_local_opts_suffix,
                         'EXEC:{ssh_command} socat STDIO UNIX-CONNECT\\:{remote_path}',
                         )
    remote_path = args.remote_path
    local_path = args.local_path or remote_path
    real_socat_command = [
        s.format(
            local_path=local_path,
            remote_path=remote_path,
            ssh_command=args.ssh_command,
        )
        for s in real_socat_command]
    logging.debug("Real socat command: %s", real_socat_command)

    logging.info("Spawning the socat process")
    os.execvp(real_socat_command[0], real_socat_command)

if __name__ == '__main__':
    main()
