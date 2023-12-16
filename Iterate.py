#!/usr/bin/env python3

import os
import subprocess


def run_tool(command, filepath):
    output_folder = "scan_results"
    os.makedirs(output_folder, exist_ok=True)

    with open(filepath, "r") as file:
        for line in file:
            domain = line.strip()
            output_file = f"{output_folder}/{command.replace(' ', '_')}_{domain.replace('.', '_')}.txt"

            try:
                process = subprocess.Popen(command.split() + [domain], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1, universal_newlines=True)

                for line in process.stdout:
                    print(line.strip(), "green"))

                for line in process.stderr:
                    print(line.strip(), "red"))

                process.wait()

                # You may want to save the output to a file if the tool doesn't do it automatically
                with open(output_file, "w") as output:
                    output.write(process.stdout.read())
            except subprocess.CalledProcessError as e:
                print(f"Error running {command} for {domain}: {e.stderr.strip()}", "red"))

def main():
    command = input("Enter the command to run (e.g., nmap -p- -T4): ")
    filepath = input("Enter the file path containing domains: ")

    run_tool(command, filepath)

if __name__ == "__main__":
    main()
