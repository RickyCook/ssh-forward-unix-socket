# ssh-forward-unix-socket

Forward a Unix socket over SSH

## Examples

In all examples, `<host>` represents a remote host.

### Forward a remote Docker socket
```bash
sudo forward_socket \
  --local_user $(id -un) \
  "ssh -i $HOME/.ssh/id_rsa $(id -un)@<host>" \
  /var/run/docker.sock
```
- Sudo so that you can create the local `/var/run/docker.sock`
- SSH into your host, with your current user's username, and your `id_rsa` (can't just use <host>, because the sudo will ssh as `root@<host>` and use root's keys)
- Listen at `/var/run/docker.sock` (the same as the remote)
- Set the listen socket's owner to your current user

### Forward a remote Docker socket, with connection pool
```bash
sudo forward_socket
  --local_user $(id -un) \
  "ssh -i $HOME/.ssh/id_rsa -o ControlMaster auto -o ControlPersist 600 -o ControlPath docker_ssh.sock $(id -un)@<host>" \
  /var/run/docker.sock
```
Mostly the same as the forwarding above, except:
- `ControlMaster auto` adds connection pooling
- `ControlPersist 600` sets the connection pool timeout to 600
- `ControlPath docker_ssh.sock` creates the shared SSH socket `docker_ssh.sock`
