#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webbrowser


class Movie:
    """
    It provides a way to store the movie relation information.
    
    Args:
        movie_title (str): the title of movie
        movie_storyline (str): the short storyline of movie
        poster_image_url (str): the poster image of movie
        trailer_youtube (str): an youtube url of the movie
    
    Method:
        show_trailer:
            open the youtube url you provided when you defined it in
            the browser. 
    """

    def __init__(self,
                 movie_title,
                 movie_storyline,
                 poster_image_url,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube

    @staticmethod
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
