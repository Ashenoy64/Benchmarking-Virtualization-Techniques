
IMG_ID=firecracker
CONTAINER_ID=$(docker run -td $IMG_ID /bin/bash)

MOUNTDIR=mnt
FS=GRPC.ext4

mkdir $MOUNTDIR
qemu-img create -f raw $FS 800M
mkfs.ext4 $FS
mount $FS $MOUNTDIR
docker cp $CONTAINER_ID:/ $MOUNTDIR
umount $MOUNTDIR
