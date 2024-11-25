#!/bin/bash

# Check if at least two arguments are provided
if [ "$#" -lt 2 ]; then
    echo "Usage: $0 <IMAGE_ID> <FS> [SIZE]"
    exit 1
fi

# Assign command-line arguments to variables
IMG_ID=$1
FS=$2
SIZE=${3:-800M}  # Default to 800M if the third argument is not provided

# Generate a container ID
CONTAINER_ID=$(docker run -td "$IMG_ID" /bin/bash)

# Define the mount directory
MOUNTDIR=mnt

# Create the mount directory if it doesn't exist
if [ ! -d "$MOUNTDIR" ]; then
    mkdir "$MOUNTDIR"
fi

# Create and format the filesystem with the specified or default size
qemu-img create -f raw "$FS" "$SIZE"
mkfs.ext4 "$FS"

# Mount the filesystem to the mount directory
mount "$FS" "$MOUNTDIR"

# Copy the container's file system to the mounted filesystem
docker cp "$CONTAINER_ID":/ "$MOUNTDIR"

# Unmount the filesystem
umount "$MOUNTDIR"
chmod 777 "$FS"
echo "Process completed successfully with FS size $SIZE."

