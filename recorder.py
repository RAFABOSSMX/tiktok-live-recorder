#!/usr/bin/env python3
import sys
import subprocess


def record_tiktok_live(url, output_path):
    """
    Record a TikTok live stream using streamlink.

    Args:
        url (str): The TikTok LIVE URL.
        output_path (str): Path to save the recorded stream (e.g., "output.ts").
    """
    cmd = ["streamlink", url, "best", "-o", output_path]
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error recording stream: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python recorder.py <tiktok_live_url> <output_file>")
        sys.exit(1)

    live_url = sys.argv[1]
    output_file = sys.argv[2]
    record_tiktok_live(live_url, output_file)
