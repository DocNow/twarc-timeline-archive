# twarc-timeline-archive

This module extends [twarc] to allow you to fetch the timelines for a list of
users (either Twitter user_ids or usernames). Unlike the `twarc2 timelines`
subcommand `twarc2 timeline-archive` is designed to be run on a schedule and
will only fetch new tweets since the last run instead of the entire timeline.

All the tweets will be written to files named after the user in the given
directory. When you run timelines successively on multiple days it is smart
enough to only fetch tweets since the last tweet that was found for the user.

    twarc timelines users.txt /path/to/a/directory

[twarc]: https://github.com/docnow/twarc
