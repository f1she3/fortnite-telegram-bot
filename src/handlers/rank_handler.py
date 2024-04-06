"""
    This module handles the fortnite ranking.
"""
import fortnite_api
from handlers import constants
from ..db.db import db_get_all_rows, db_update_stats


async def get_ranking():
    """
    Generates the new ranking from the newly data fetched from the API.
    """
    # Fetch the old stats
    players = []
    api = fortnite_api.FortniteAPI(
        api_key=constants.FORTNITE_API_KEY,
        run_async=True
    )
    db_users = db_get_all_rows("players")
    for user in db_users:
        # Fetch the new stats
        latest_stats = await api.stats.fetch_by_name(
            user['fortnite_username']
        )
        # Get a summary for the previous time period
        player = get_player_summary(user, latest_stats)
        players.append(player)

        update_player_stats(user['tg_id'], latest_stats)

    ranked_players = sorted(
        players,
        key=lambda d: d['ratio'],
        reverse=True
    )

    return ranked_players


def get_player_summary(db_item, latest_stats):
    """
    Get the delta between previous period and today.
    """
    new_kill_count = latest_stats.stats.all.overall.kills - \
        latest_stats.stats.all.solo.kills
    monthly_kills = new_kill_count - db_item['kills']

    new_death_count = latest_stats.stats.all.overall.deaths - \
        latest_stats.stats.all.solo.deaths
    monthly_deaths = new_death_count - db_item['deaths']
    if monthly_deaths != 0:
        monthly_ratio = monthly_kills / monthly_deaths
    else:
        if monthly_kills == 0:
            monthly_ratio = 0
        else:
            monthly_ratio = 100

    new_match_count = latest_stats.stats.all.overall.matches - \
        latest_stats.stats.all.solo.matches
    monthly_matches = new_match_count - db_item['matches']

    # Save a summary for every player
    player = {
        "name": db_item['fortnite_username'],
        "ratio": monthly_ratio,
        "kills": monthly_kills,
        "deaths": monthly_deaths,
        "matches": monthly_matches
    }

    return player

def update_player_stats(tg_id, latest_stats):
    """
    Update a user's stats with new data fetched from API.
    """
    new_kill_count = latest_stats.stats.all.overall.kills - \
        latest_stats.stats.all.solo.kills
    new_death_count = latest_stats.stats.all.overall.deaths - \
        latest_stats.stats.all.solo.deaths
    new_match_count = latest_stats.stats.all.overall.matches - \
        latest_stats.stats.all.solo.matches

    db_update_stats(
        tg_id=tg_id,
        new_kill_count=new_kill_count,
        new_death_count=new_death_count,
        new_match_count=new_match_count
    )

async def get_ranking_msg():
    """
    Get the ranking's formated message to display on the tg group.
    """
    ranking_emojis = [
        "🥇",
        "🥈",
        "🥉",
        "🐐"
    ]
    ranked_players = await get_ranking()
    msg = "<code>Classement mensuel</code>\n\n"
    for i,player in enumerate(ranked_players):
        if i < len(ranking_emojis):
            msg += f"{ranking_emojis[i]} {player['name']}"
            msg += " - "
            msg += f"ratio: {round(player['ratio'], 2)}; kills: {player['kills']}; parties: {player['matches']}\n"
        else:
            msg += f"{player['name']}"
            msg += " - "
            msg += f"ratio: {round(player['ratio'], 2)}; kills: {player['kills']}; parties: {player['matches']}\n"

    return msg
