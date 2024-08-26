#!/bin/bash

# Define the GRPC directory path
grpc="/home/user/GRPC/Go"

# Check if the GRPC directory exists
if [ ! -d "$grpc" ]; then
    echo "GRPC directory does not exist: $grpc"
    exit 1
fi

# Change to the GRPC directory
cd "$grpc" || exit

# Check if the Clients directory exists, if not, create it
if [ ! -d "Clients" ]; then
    mkdir OPS
    echo "Created Clients directory."
else
    echo "Clients directory already exists."
fi

# Function to build the Go client and move the binary to the Clients directory
build_and_move() {
    local service_dir="$1"
    local output_name="$2"
    local main_file="$3"

    cd "$service_dir" || exit
    go build -o "$output_name" "$main_file"
    mv "$output_name" ../OPS
    echo "Built and moved $output_name to OPS directory."
    cd ..
}

# Build and move binaries for different services
build_and_move "BiStreaming" "BiStreamingServer" "Server.go"
build_and_move "ServerStreaming" "ServerStreamingServer" "Server.go"
build_and_move "ClientStreaming" "ClientStreamingServer" "server.go"
build_and_move "Unary" "UnaryServer" "server.go"

echo "All clients built and moved successfully."

