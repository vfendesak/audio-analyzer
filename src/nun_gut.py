import json
from tqdm import tqdm


def main():

    with open("output/transcripts.json", "r") as file:
        transcripts = json.load(file)

    ng_counter = 0

    for _, transcript in tqdm(transcripts.items(), ncols=60):
        if "nun gut" in transcript.lower():
            ng_counter += 1
            print(f"nun gut {ng_counter}")

if __name__ == "__main__":
    main()