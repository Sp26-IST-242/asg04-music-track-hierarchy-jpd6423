"""
A collection class that holds MusicTrack objects (Songs and Podcasts).

Design notes:
  • _tracks is kept private (single underscore) and exposed as a *copy*
    through the `tracks` property to protect encapsulation.
  • clear_playlist() uses list.clear() rather than rebinding to None or a new
    list, so the internal object reference stays valid.
  • sort_by_release_year() delegates to list.sort(), which in turn calls
    MusicTrack.__lt__ — the comparison logic defined in Part 3 pays off here.
  • __str__ uses a generator expression with str.join() for a concise
    multi-line string without building an intermediate list manually.
"""
from music_track import MusicTrack

class Playlist:
    def __init__(self):
        self._tracks: list[MusicTrack] = []

    # adds track to tracks
    def add_track(self, track: MusicTrack):
        self._tracks.append(track)

    # clears playlist
    def clear_playlist(self):
        self._tracks.clear()

    def sort_by_release_year(self):
        self._tracks.sort()

    @property
    def tracks(self) -> list[MusicTrack]:
        return list(self._tracks)
    
    def __str__(self):
        return "\n".join(str(i) for i in self._tracks)