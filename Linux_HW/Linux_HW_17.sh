#!/bin/sh

if [ -z "$1" ]; then
  echo "using: $0 <host>"
  exit 1
fi

HOST="$1"
FAIL_COUNT=0

while :
do
  PING_OUTPUT=$(ping -c 1 -W 1 "$HOST" 2>&1)

  if echo "$PING_OUTPUT" | grep -q "time="; then
    TIME=$(echo "$PING_OUTPUT" | sed -n 's/.*time=\([0-9.]*\).*/\1/p')

    echo "Ping: ${TIME} ms"

    FAIL_COUNT=0

    TIME_INT=$(printf "%.0f" "$TIME")

    if [ "$TIME_INT" -gt 100 ]; then
      echo "⚠️ ping time over 100 ms!"
    fi

  else
    echo "❌ ping error"

    FAIL_COUNT=$((FAIL_COUNT + 1))

    if [ "$FAIL_COUNT" -ge 3 ]; then
      echo "🚨 3 failed pings in a row!"
    fi
  fi
  sleep 1
done
