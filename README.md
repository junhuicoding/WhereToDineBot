# WhereToDineBot
A work in progress of a Telegram bot that will recommend a place for you to dine at.
This bot was motivated by the difficulties in choosing a place to eat, especially when dining as a group, due to people's tendency to say "Anything", "You decide la!", etc.
When available, this bot is online at @WhereToDineBot on Telegram.

## Technical Details
The bot uses [python-telegram-bot](https://python-telegram-bot.readthedocs.io/) to communicate with Telegram servers.
This bot queries the Google Places API. To run it, you will need a Google Places API Key.
A Telegram Token is required to connect it to Telegram.

## Installation
Create a `keys.py` file in the root directory with the values:
```python
TOKEN = "<TELEGRAM TOKEN>"
GOOGLE_PLACES_API_KEY = "<GOOGLE PLACES API KEY>"
```
Install the required packages:
- python-telegram-bot
- requests

Run it!

## Planned Features
- A more robust recommendation system that allows user to reject current recommendation, and generate a new one
- Allow parameters such as type of food and radius of search
- Through a database, allow storing of visited places to improve future recommendations
- Dockerise it for easier deployment
- Improve logger to parse UTF-16 chars


## Contributing
Fork it!
- Create your feature branch: git checkout -b my-new-feature
- Commit your changes: git commit -am 'Add some feature'
- Push to the branch: git push origin my-new-feature
- Submit a pull request :D

## License
The MIT License (MIT)

Copyright (c) 2015 Chris Kibble

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.