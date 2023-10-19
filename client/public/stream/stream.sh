VIDSOURCE="rtsp://192.168.0.113:554/user:1cinnovation;pwd:1cinnovation123"
AUDIO_OPTS="-c:a aac -b:a 160000 -ac 2"
VIDEO_OPTS="-s 854x480 -c:v libx264 -b:v 800000"
OUTPUT_HLS="-hls_time 150 -hls_list_size 10 -start_number 1 -hls_delete_threshold 3 -hls_flags delete_segments"
SEGMENT_OPTS="-c copy -map 0 -f segment -strftime 1 -segment_time 60 -segment_format mp4 \"%Y%m%d-%H%M.mp4\""

ffmpeg -i "$VIDSOURCE" -y $AUDIO_OPTS $VIDEO_OPTS $OUTPUT_HLS playlist.m3u8
