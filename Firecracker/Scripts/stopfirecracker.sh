#!/bin/bash

# Path to Firecracker API socket
API_SOCKET="/tmp/firecracker.sock"

# Stop the Firecracker instance
curl -X PUT --unix-socket "${API_SOCKET}" \
    --data '{"action_type": "SendCtrlAltDel"}' \
    "http://localhost/actions"

# Wait a few seconds to ensure the instance has stopped
sleep 2

# Find and kill the Firecracker process
FC_PID=$(ps aux | grep '[f]irecracker' | awk '{print $2}')
if [ -n "$FC_PID" ]; then
    kill -9 "$FC_PID"
fi

# Clean up TAP device
sudo ip link del tap0

echo "Firecracker instance stopped and resources cleaned up."

