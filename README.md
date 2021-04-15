# twarc-timelines

This module extends twarc to allow you to fetch the timelines for a list of
users (either Twitter user_ids or usernames) stored in a text file. Every time
you run `twarc timelines` with a given list of users it will write out their
tweets as JSONL named after the username.

[twarc]: https://github.com/docnow/twarc
