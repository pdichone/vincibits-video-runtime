import os
from moviepy.editor import VideoFileClip

video_folder_path = "add_video_folder_path_here"

video_file_path = "video_titles_txt"


def format_duration(seconds):
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    # 02:34 minutes
    return f"{minutes}:{seconds:02d} mins"


def get_total_runtime_and_titles(folder_path, output_path):
    total_duration = 0
    video_details = []

    for filename in os.listdir(folder_path):
        if filename.endswith((".mp4", ".avi", ".mov", ".mkv")):
            try:
                filepath = os.path.join(folder_path, filename)
                video = VideoFileClip(filepath)
                video_duration = video.duration
                total_duration += video_duration
                video.close()
                # lesson-1.mp4 -> lesson-1

                title_without_extension = os.path.splitext(filename)[0]

                # lesson-1 -> Lesson 1 - 3:45 mins
                formatted_duration = format_duration(video_duration)

                video_details.append((title_without_extension, formatted_duration))
            except Exception as e:
                print(f"Error processing {filename}: {e}")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"Total duration: {format_duration(total_duration)}\n")
        f.write(f"Total videos: {len(video_details)}\n")
        for title, duration in video_details:
            f.write(f"{title} - {duration}\n")

    return total_duration / 60


total_minutes = get_total_runtime_and_titles(video_folder_path, video_file_path)
print(f"Total runtime of all videos: {total_minutes:.2f} minutes")
