
import moviepy.editor as mp


import moviepy.editor as mp

# 采样率16k 保证和paddlespeech一致
def extract_audio(videos_file_path):
     my_clip = mp.VideoFileClip(videos_file_path,audio_fps=16000)
     if (videos_file_path.split(".")[-1] == 'MP4' or videos_file_path.split(".")[-1] == 'mp4'):
          p = videos_file_path.split('.MP4')[0]
          my_clip.audio.write_audiofile(p + '_video.wav')
          new_path = p + '_video.wav'
     return new_path

if __name__ == '__main__':
    # 拿到新生成的音频的路径
    path = extract_audio('/media/hxzh02/mobilePan/AICA6首席架构师计划/预科班/AICA6－产业中NLP任务的技术选型与落地.mp4')
