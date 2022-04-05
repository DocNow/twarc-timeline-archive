import json
import click
import pathlib
import datetime


@click.command("timeline-archive")
@click.option(
    "--use-search",
    is_flag=True,
    default=False,
    help="Use the search/all API endpoint which is not limited to the last 3200 tweets, but requires Academic Product Track access.",
)
@click.argument("infile", type=click.File("r"), default="-")
@click.argument("output_dir", type=str, default="timelines")
@click.pass_obj
def timeline_archive(T, infile, output_dir, use_search):
    """
    Fetch the timelines for every username or userid in a file.
    """

    output_dir = pathlib.Path(output_dir)
    if not output_dir.is_dir():
        output_dir.mkdir(parents=True)

    for line in infile:
        line = line.strip()
        since_id = get_max_tweet_id(line, output_dir)
        click.echo(f"🌟  fetching timeline for {line} since {since_id}")

        try:
            # which api endpoint to use
            if use_search and since_id:
                tweets = T.search_all(f"from:{line}", since_id=since_id)
            elif use_search:
                tweets = T.search_all(
                    f"from:{line}",
                    start_time=datetime.datetime(
                        2006, 3, 21, tzinfo=datetime.timezone.utc
                    ),
                )
            else:
                tweets = T.timeline(line, since_id=since_id)

            for response in tweets:
                write_response(line, response, output_dir)
        except Exception as e:
            click.echo(
                click.style(
                    f"💥  Error fetching timeline for {line} since {since_id}, {e}",
                    fg="red",
                ),
                err=True,
            )


file_handles = {}


def write_response(user, response, output_dir):
    fh = file_handles.get(user)
    if not fh:
        fh = get_json_file(user, output_dir).open("a")
        file_handles[user] = fh
    fh.write(json.dumps(response) + "\n")


def get_max_tweet_id(user, output_dir):
    """
    Look in a file for the largest tweet id.
    """
    max_tweet_id = None
    json_file = get_json_file(user, output_dir)
    if json_file.is_file():
        for line in json_file.open("r"):
            response = json.loads(line)
            for tweet in response["data"]:
                if max_tweet_id is None or int(tweet["id"]) > max_tweet_id:
                    max_tweet_id = int(tweet["id"])
    return max_tweet_id


def get_json_file(user, output_dir):
    return pathlib.Path(output_dir / f"{user}.jsonl")
