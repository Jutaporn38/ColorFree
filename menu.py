#!/bin/bash

# Install figlet if not already installed
pkg install figlet

# Function to print colored ASCII text
print_colored_text() {
  color_code=$1
  text=$2
  echo -e "\033[${color_code}m$(figlet -f slant "${text}")\033[0m"
}

# Main function
while true; do
  clear
  echo "Select an option:"
  echo "1) Green text"
  echo "2) Blue text"
  echo "3) Red text"
  echo "4) Exit"

  read -p "Enter your choice: " option

  case $option in
    1)
      print_colored_text "32" "Hello my hacker"  # Green color
      ;;
    2)
      print_colored_text "34" "Hello my hacker"  # Blue color
      ;;
    3)
      print_colored_text "31" "Hello my hacker"  # Red color
      ;;
    4)
      echo "Exiting..."
      exit 0
      ;;
    *)
      echo "Invalid option, please try again."
      ;;
  esac

  read -p "Press Enter to continue..." dummy
done
