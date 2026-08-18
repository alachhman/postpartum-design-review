#!/bin/zsh
# Screenshots one phone mock at 1:1.  usage: ./scripts/shot.sh <page.html> <stageIndex> <outName>
CHROME="${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"
OUT="${SHOT_OUT:-./.shots}"; mkdir -p "$OUT"
"$CHROME" --headless --disable-gpu --hide-scrollbars --force-device-scale-factor=2 \
  --window-size=440,900 --virtual-time-budget=7000 \
  --screenshot="$OUT/$3.png" "http://localhost:8731/$1?shot=$2" 2>/dev/null
echo "$OUT/$3.png"
