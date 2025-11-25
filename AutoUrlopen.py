import webbrowser
import time

def main():
    print("")

    video_url = input(" Enter a URL: ").strip()
    if not video_url.startswith("http"):
        print("Invalid URL. Exiting Sadly.")
        return

    total_views = 50
    wait_time = 35  # seconds

    for i in range(1, total_views + 1):
        print(f"\n Opening video {i}/{total_views}: {video_url}")
        webbrowser.open(video_url)
        if i < total_views:
            print(f" Waiting {wait_time} seconds before next open...")
            time.sleep(wait_time)

    print("\n Done...")

if __name__ == "__main__":
    main()