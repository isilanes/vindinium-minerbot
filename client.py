# -*- coding: utf-8 -*-

import sys
import time
import requests
import argparse

from libvindinium import Bot
from libvindinium import utils

#------------------------------------------------------------------------------#

# Read arguments:
parser = argparse.ArgumentParser()

parser.add_argument("--key",
        help="User key. Default: None.",
        default=None)

parser.add_argument("--arena",
        help="Compete on arena. Default: training.",
        action="store_true",
        default=False)

parser.add_argument("--number",
        help="Number of games (if arena) or turns (if training). Default: 100.",
        type=int,
        default=100)

parser.add_argument("--server",
        help="Server URL to connect to. Default: http://vindinium.org.",
        default="http://vindinium.org")

parser.add_argument("--user-id",
        help="User ID. Default: 6ma0lt4d (isilanes).",
        default="6ma0lt4d")

o = parser.parse_args()

#--------------------------------------------------------------------------------#

def get_new_game_state(session, server_url, key, mode='training', number_of_turns=10):
    """Get a JSON from the server containing the current state of the game"""

    if mode == 'training':
        # Don't pass the 'map' parameter if you want a random map:
        params = { 'key': key, 'turns': number_of_turns, 'map': 'm1'}
        api_endpoint = '/api/training'
    else:
        params = { 'key': key}
        api_endpoint = '/api/arena'

    # Wait for 10 minutes:
    time.sleep(1.0)
    r = session.post(server_url + api_endpoint, params, timeout=10*60)

    if r.status_code == 200:
        return r.json()
    else:
        print("Error when creating the game")
        print(r.text)

def move(session, url, direction):
    """Send a move to the server.
    Moves can be one of: 'Stay', 'North', 'South', 'East', 'West'"""

    try:
        r = session.post(url, {'dir': direction}, timeout=15)

        if r.status_code == 200:
            return r.json()
        else:
            print("Error HTTP %d\n%s\n" % (r.status_code, r.text))
            return {'game': {'finished': True}}
    except requests.exceptions.RequestException as e:
        print(e)
        return {'game': {'finished': True}}

def is_finished(state):
    """Return True if game is finished, False otherwise."""

    return state['game']['finished']

def run_game(o, mode, turns, bot):
    """Starts a game with all the required parameters."""

    # Create a requests session that will be used throughout the game:
    session = requests.session()

    if mode == 'arena':
        print('Connected and waiting for other players to join...')

    # Get the initial state
    state = get_new_game_state(session, o.server, o.key, mode, turns)
    print("Playing at: " + state['viewUrl'])

    every = 10
    i = 0
    while not is_finished(state):
        i += 1

        # Some nice output ;)
        if i >= every:
            sys.stdout.write('.')
            sys.stdout.flush()
            i = 0
        sys.stdout.flush()

        # Choose a move:
        direction = bot.move(state)

        # Send the move and receive the updated game state:
        url = state['playUrl']
        state = move(session, url, direction)
        time.sleep(0.1) # do not loop too fast

    # Clean up the session
    session.close()

    # Save current elo:
    try:
        utils.save_elo(state, o)
    except:
        # No worries if we can't:
        pass

    try:
        return utils.my_result(state, o)
    except:
        return None


if __name__ == "__main__":
    #if len(sys.argv) < 4:
    #    print("Usage: %s <key> <[training|arena]> <number-of-games|number-of-turns> [server-url]" % (sys.argv[0]))
    #    print('Example: %s mySecretKey training 20' % (sys.argv[0]))

    # User key:
    if not o.key:
        print("User key is required!")
        exit()

    # Game mode:
    mode = "training"
    if o.arena:
        mode = "arena"

    # Number of games and turns:
    if mode == "training":
        number_of_games = 1
        number_of_turns = o.number
    else: 
        number_of_games = o.number
        number_of_turns = 300 # ignored in arena mode

    # Execute run loop:
    for i in range(number_of_games):
        result = run_game(o, mode, number_of_turns, Bot.MinerBot())
        string = "\nGame finished: {0}/{1} - Result: {2}\n".format(i+1, number_of_games, result)
        print(string)
