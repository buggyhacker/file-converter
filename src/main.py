import argparse
from src.converter.audio import convert_audio
from src.converter.images import convert_image
from src.converter.text import convert_text
from src.converter.video import convert_video

def main():
    parser = argparse.ArgumentParser(description="Your secure file conversion tool")

    parser.add_argument(
        '--convert', 
        choices=['image', 'text', 'audio', 'video'], 
        help='Specify the type of conversion'
    )
    
    parser.add_argument('--image', help='Convert images such as .png -> .jpeg')
    parser.add_argument('--text', help='Convert text files such as .csv -> .json')
    parser.add_argument('--audio', help='Convert audio files such as .wav -> .mp3')
    parser.add_argument('--video', help='Convert video files such as .mp4 -> .avi')

    args = parser.parse_args()

    if args.convert == 'image' and args.image:
        convert_image(args.image)
    elif args.convert == 'text' and args.text:
        convert_text(args.text)
    elif args.convert == 'audio' and args.audio:
        convert_audio(args.audio)
    elif args.convert == 'video' and args.video:
        convert_video(args.video)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()