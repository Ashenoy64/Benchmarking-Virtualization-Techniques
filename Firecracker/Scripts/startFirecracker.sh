API_SOCKET="/tmp/firecracker.sock"

sudo rm -f $API_SOCKET

../firecracker --api-sock  "${API_SOCKET}"
