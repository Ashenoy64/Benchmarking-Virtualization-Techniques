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
    mkdir Clients
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
    mv "$output_name" ../Clients
    echo "Built and moved $output_name to Clients directory."
    cd ..
}

# Build and move binaries for different services
build_and_move "BiStreaming" "BiStreamingClient" "BiStreamClient.go"
build_and_move "ServerStreaming" "ServerStreamingClient" "ServerStreamClient.go"
build_and_move "ClientStreaming" "ClientStreamingClient" "ClientStreamClient.go"
build_and_move "Unary" "UnaryClient" "UnaryClient.go"

echo "All clients built and moved successfully."

