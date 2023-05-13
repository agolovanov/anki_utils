def convert_audio_tag(s : str):
    """
    Converts from format [sound:str.mp3] to <audio src="str.mp3"></audio>
    """
    prefix = '[sound:'
    postfix = ']'
    if s.startswith(prefix) and s.endswith(postfix):
        s = s[len(prefix):-len(postfix)]
        return f'<audio src="{s}"></audio>'