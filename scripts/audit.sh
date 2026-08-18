#!/bin/zsh
# Reports content overflowing the 852pt phone canvas and tap targets under 44pt.
# usage: ./scripts/audit.sh 01-home.html [more.html ...]   (server must be on :8731)
CHROME="${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"
for f in "$@"; do
  R=$("$CHROME" --headless --disable-gpu --virtual-time-budget=6000 --dump-dom \
      "http://localhost:8731/$f?audit=1" 2>/dev/null \
      | grep -o '<div id="AUDIT">[^<]*' | sed 's/<div id="AUDIT">//')
  echo "$f :: ${R:-<no audit marker>}"
done
