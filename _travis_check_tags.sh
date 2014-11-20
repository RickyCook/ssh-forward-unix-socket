#!/bin/bash
tag=$(git describe --tags --exact-match 2>/dev/null)
if [[ $? -ne 0 ]]; then
  echo "Untagged! Everything is fine here"
  exit 0
fi

python <<END
from pkg_resources import require
tag = '$tag'
version = tag[1:]
require('ssh-forward-unix-socket==%s' % version)
END
