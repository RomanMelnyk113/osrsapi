import requests

from . import const


class Stats:
    def stats_for_infernal(rsn):
        uri = const.HISCORES_URL + str(rsn)
        try:
            response = requests.get(uri)
            stats_array = response.content.decode().replace("\n", ",").split(",")
            final_stats = {
                'defence': stats_array[7],
                'hitpoints': stats_array[13],
                'ranged': stats_array[16],
                'prayer': stats_array[19],
                'magic': stats_array[22],
            }
        except requests.HTTPError:
            raise Exception("Unable to find player with rsn %d." % rsn)


        return final_stats
