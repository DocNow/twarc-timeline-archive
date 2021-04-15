import re
import json
import twarc
import click
import pathlib

@click.command('timelines')
@click.option('--output-dir', type=str, 
    help='Write tweets to user specific files in directory')
@click.argument('infile', type=click.File('r'), default='-')
@click.argument('outfile', type=click.File('w'), default='-')
@click.pass_obj
def timelines(T, infile, output_dir, outfile):
    """
    Fetch the timelines for every username or userid in a file.
    """

    if output_dir:
        output_dir = pathlib.Path(output_dir)
        if not output_dir.is_dir():
            output_dir.mkdir(parents=True)

    for line in infile:
        line = line.strip()
        usernames = False if re.match(r'^\d+$', line) else True
        if output_dir:
            since_id = get_max_tweet_id(line, output_dir)
            click.echo(f'🌟  fetching timeline for {line} since {since_id}')
        else:
            since_id = None

        for response in T.timeline(line, since_id=since_id):
            if output_dir:
                write_response(line, response, output_dir) 
            else:
                click.echo(json.dumps(response) + "\n", file=outfile)

file_handles = {}
def write_response(user, response, output_dir):
    fh = file_handles.get(user)
    if not fh:
        fh = get_json_file(user, output_dir).open('a')
        file_handles[user] = fh
    fh.write(json.dumps(response) + "\n")

def get_max_tweet_id(user, output_dir):
    """
    Look in a file for the largest tweet id.
    """
    max_tweet_id = None
    json_file = get_json_file(user, output_dir)
    if json_file.is_file():
        for line in json_file.open('r'):
            response = json.loads(line)
            for tweet in response['data']:
                if max_tweet_id is None or int(tweet['id']) > max_tweet_id:
                    max_tweet_id = int(tweet['id'])
    return max_tweet_id

def get_json_file(user, output_dir):
    return pathlib.Path(output_dir / f'{user}.jsonl')
