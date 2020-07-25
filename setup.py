import cx_Freeze

executables = [cx_Freeze.Executable("snake1.py")]

cx_Freeze.setup(
    name="Snake",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["icon.png","pic1.jpg","pic.png","over.jpg","highscore.txt",
                                            "back.mp3","first.mp3","song.mp3","song1.mp3","song2.mp3",
                                            "song3.mp3","song4.mp3","song5.mp3","song6.mp3","song7.mp3",
                                            "song8.mp3","song9.mp3","song10.mp3","start.mp3"]}},
    executables = executables

    )

