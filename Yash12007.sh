#!/bin/bash

function run_super_scan() {
    echo "Running Super Scan..."
    echo "[Info]: Scanning with version 1.0"

    if [ -z "$1" ]; then
    echo "[Info]: Usage: $0 <target>"
    exit 1
    fi

    target="$1"
    echo "[Info]: Scanning all 65535 ports on $target..."
    echo "[Info]: Checking for nmap, lsusb & adb"
    sudo apt install nmap -y
    sudo apt install adb -y
    nmap -p 1-65535 "$target"
    adb start-server
    adb devices
    adb devices -l
    lsusb
}

function help_command() {
    cat << "EOF"
Commands:
    [q] = Quit
    [r] = Run Super Scan
    [h] = Help
    [d] = Online Documentation
    [p] = Projects on Github
    [a] = Applications for Windows/Android
    [ps] = Port Scanning
    [ut] = Update Tools (All tools inside of apt)
    [-w] = Open Official website
    
EOF
}

function online_documentation() {
    echo "Opening online documentation..."
    xdg-open "https://yash12007.github.io/Max"
}

function projects_on_github() {
    echo "Opening projects on Github..."
    xdg-open "https://www.github.com/Yash12007"
}

function applications() {
    echo "Opening website, If the website isn't open then click on this url https://yash12007.github.io/home"
    xdg-open "https://yash12007.github.io/"
}

function port_scanning() {
    # Check if the user provided the target IP/hostname as an argument
    if [ -z "$1" ]; then
    echo "Usage: $0 <target>"
    exit 1
    fi

    target="$1"
    echo "Scanning all 65535 ports on $target..."
    sudo apt install nmap -y
    nmap -p 1-65535 "$target"
}

function update_tools() {
    echo "Updating tools (All tools inside of apt)..."
    sudo apt update && sudo apt upgrade -y &
}

function open_website() {
    echo "Opening website, If the website isn't open then click on this url https://yash12007.github.io/home"
    xdg-open "https://yash12007.github.io/"
}

function quit_command() {
    echo "Goodbye!"
    exit 0
}

# Display ASCII art and help commands
clear
cat << "EOF"

██    ██  █████  ███████ ██   ██  ██ ██████   ██████   ██████  ███████ 
 ██  ██  ██   ██ ██      ██   ██ ███      ██ ██  ████ ██  ████      ██ 
  ████   ███████ ███████ ███████  ██  █████  ██ ██ ██ ██ ██ ██     ██  
   ██    ██   ██      ██ ██   ██  ██ ██      ████  ██ ████  ██    ██   
   ██    ██   ██ ███████ ██   ██  ██ ███████  ██████   ██████     ██   
________________________________________________________________________

                Yash12007: Technology you need
________________________________________________________________________

Welcome to Yash12007, a software development company dedicated to providing
high-quality software solutions to businesses and organizations of all sizes.
We are passionate about software development and strive to create innovative
and intuitive software that empowers our clients to achieve their goals and
streamline their operations.
 
    Follow us on YouTube: https://www.youtube.com/@Yash12007

Commands:
    [q] = Quit
    [r] = Run Super Scan
    [h] = Help
    [d] = Online Documentation
    [p] = Projects on Github
    [a] = Applications for Windows/Android
    [ps] = Port Scanning
    [ut] = Update Tools (All tools inside of apt)
    [-w] = Open Official website
    
EOF

while true; do
    read -p "Enter a command: " command

    case "$command" in
        "r") read -p "Enter the target IP/hostname: " target_ip; run_super_scan "$target_ip" ;;
        "h") help_command ;;
        "d") online_documentation ;;
        "p") projects_on_github ;;
        "a") applications ;;
        "ps") read -p "Enter the target IP/hostname: " target_ip; port_scanning "$target_ip" ;;
        "ut") update_tools ;;
        "-w") open_website ;;
        "q") quit_command ;;
        *)
            echo "Error: Invalid command. Type 'h' for help."
            ;;
    esac
done
