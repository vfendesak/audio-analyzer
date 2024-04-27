from model import AudioAnalyzer
from pathlib import Path
import json
from tqdm import tqdm


def main():
    aa = AudioAnalyzer()
    transcripts = {}

    for audio in tqdm((Path(__file__).parent / "input").iterdir(), ncols=60):
        transcripts[audio.name] = aa.transcribe(str(audio))

    with open("output/transcripts.json", "w") as output_file:
        json.dump(transcripts, output_file)


if __name__ == "__main__":
    main()
