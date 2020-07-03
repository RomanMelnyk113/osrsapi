# OSRS API wrapper Python

## Usage

```python
>>> from osrs_api import GrandExchange
>>> from osrs_api import Item
>>> whip_id = Item.get_ids('abyssal whip')
>>> whip_id
4151
>>> whip = GrandExchange.item(whip_id)
>>> whip.description
'A weapon from the abyss.'
>>> whip.price(), whip.is_mem
(1648785, True)
>>> thirty_days = whip.price_info.trend_30
>>> thirty_days.trend, thirty_days.change
('negative', -18.0)
>>> dagger_ids = Item.get_ids('rune dag')
# If you enter a partial name, you will get a list of all possible matches.
>>> dagger_ids
[5696, 5678, 1229, 1213]
# Names
>>> [Item.id_to_name(id) for id in dagger_ids]
['Rune dagger(p++)', 'Rune dagger(p+)', 'Rune dagger(p)', 'Rune dagger']
>>> GrandExchange.item(dagger_ids[0]).description
'The blade is covered with a nasty poison.'
```

### Virtualenv
You can use `poetry` tool for development:
 - install `poetry` first. See https://python-poetry.org/docs/
 - install dependencies: `poetry install`
 - open virtualenv shell: `poetry shell` (optional)
 
 
 