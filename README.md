# twarc-timelines

This module extends twarc to allow you to fetch the timelines for a list of
users (either Twitter user_ids or usernames). By default the tweets will be
written to a single file or stdout.

    pip install twarc-timelines
    twarc timelines users.txt > tweets.jsonl

However if you use the `--output-dir` option the tweets will be written to
files named after the user in the given directory. When you run timelines
successively on multiple days it is smart enough to only fetch tweets since the
last tweet that was found for the user.

    twarc timelines users.txt --output-dir /path/to/a/directory

[twarc]: https://github.com/docnow/twarc
