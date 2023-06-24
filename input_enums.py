from enum import Enum


class Options(Enum):
    SORT_VIDEOS = 1
    COMMIT_TO_REMOTE = 2
    SEARCH_FOR_VIDEO = 3
    VALIDATE_NDJSON = 4
    DOWNLOAD_AND_UPLOAD = 5
    REMOVE_DUPLICATES = 6
    EXIT = 99
    ADD_TO_DATABASE = 8
