#!/usr/bin/env python3
import yaml
import sys
import os

if __name__ == '__main__':
    input_path = os.environ.get("INPUT_FILE")
    with open(input_path) as input_file:
        dep = yaml.load(input_file, yaml.FullLoader)
        print("Dependencies:")
        print(dep)
        with open(os.environ.get("GITHUB_ENV"), "a") as env_file:
            for key, value in dep.items():
                env_file.write(f"{key}={value}\n")
