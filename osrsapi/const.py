BASE_URL = "https://secure.runescape.com"

BASE_OSRS_URL_GE = BASE_URL + "/m=itemdb_oldschool/"
BASE_RS3_URL_GE = BASE_URL + "/m=itemdb_rs/"

GE_BY_ID_PATH = "api/catalogue/detail.json?item="
GE_ICON_PATH = "obj_sprite.gif?id="
GE_LARGE_ICON_PATH = "obj_big.gif?id="
GE_GRAPH_BY_ID_PATH = "api/graph/"


def get_by_id_url(id: int, is_rs3=False):
    db_version = BASE_RS3_URL_GE if is_rs3 else BASE_OSRS_URL_GE
    base = f"{db_version}{GE_BY_ID_PATH}{id}"
    return base

def get_graph_by_id_url(id: int, is_rs3=False):
    db_version = BASE_RS3_URL_GE if is_rs3 else BASE_OSRS_URL_GE
    base = f"{db_version}{GE_GRAPH_BY_ID_PATH}{id}.json"
    return base

def get_icon_url(id: int, large=False, is_rs3=False):
    db_version = BASE_RS3_URL_GE if is_rs3 else BASE_OSRS_URL_GE
    icon_type = GE_LARGE_ICON_PATH if large else GE_ICON_PATH
    base = f"{db_version}{icon_type}{id}"
    return base