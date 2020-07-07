# OSRS API wrapper Python

## Usage

```python
from osrsapi import GrandExchange
whip_id = 1
whip = GrandExchange.item(whip_id)
print(whip.description) # ->>> 'A weapon from the abyss.'
print(whip.price(), whip.is_mem) # ->>> (1648785, True)
thirty_days = whip.price_info.trend_30
print(thirty_days.trend, thirty_days.change) # ->>> ('negative', -18.0)
```

### Virtualenv
You can use `poetry` tool for development:
 - install `poetry` first. See https://python-poetry.org/docs/
 - install dependencies: `poetry install`
 - open virtualenv shell: `poetry shell` (optional)
 
 
 