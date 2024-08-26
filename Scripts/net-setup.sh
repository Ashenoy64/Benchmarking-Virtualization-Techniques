ip link set dev eth0 up
ip addr add 172.16.0.2/30 dev eth0
ip route add default via 172.16.0.1
