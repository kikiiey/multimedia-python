from pydub import AudioSegment
audio = AudioSegment.from_file('bumbayah.mp3')
audio.export('result.mp3',format='mp3')
clipped_audio = audio[:10000]
clipped_audio.export('clipped_result.mp3', format='mp3')
combined_audio = audio + clipped_audio
combined_audio.export('combined_result.mp3', format='mp3')
audio.export('result.wav', format='wav')
louder_audio = audio + 10 
louder_audio.export('louder_result.mp3', format='mp3')