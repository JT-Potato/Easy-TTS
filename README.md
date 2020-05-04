# Easy-TTS
Make your own voice. this project is proving far harder than I originally thought. There are a few segments to this program:
1. Text to custom grapheme
  This turns text input into a series of sound representations (graphemes)
2. File Caller
  This takes the graphemes and searches for the correct series of audio files to play
3. Vocoder
  This takes the sounds, stitches them together and smoothens the audio out, before creating a new file.
  
The goal is to eliminate the need for CUDA or Tensor reliant parts of the program. There are many that will function better than this, but they rely on NVIDIA's AI software and specialised hardware, which not everybody has access to.
