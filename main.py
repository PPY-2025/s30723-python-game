import argparse

def main():
    parser = argparse.ArgumentParser(description="Prosty skrypt obsługujący --help i -h.")
    parser.add_argument('--version', action='version', version='1.0.0')
    args = parser.parse_args()

if __name__ == "__main__":
    main()
