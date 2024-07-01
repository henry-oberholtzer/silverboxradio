# SilverBoxRadio

A website intended as a template for internet radio stations of all sizes

## Features
  - User authentication with JWT
  - SQLite database
  - Shows with Episodes

## Upcoming Features
  - Client
  - 

## Contributing

#### Running the API
- Ensure Python3.12 is installed
- Configure the .env file
- In `/api` you will need to generate a secret key for the .env
```
$ python
>>> import secrets
>>> secrets.SystemRandom().getrandbits(128)
YOUR_SECRET_KEY_WILL_BE_HERE
```
- Change `dotenv` to `.env` and paste your secret key in "SECRET_KEY". Set other configuration settings as needed.
- Follow the commands below to install and get flask running.
```
$ cd ./api
$ python3.12 -m venv .venv
# Next line is for MacOS / Linux
$ source .venv/bin/activate
# On Windows run the following.
$ source .venv/Scripts/activate
$ pip install -r requirements.txt
$ flask run
```

#### Running the Client

```
$ cd ./client
$ npm install
$ npm run dev
```

## Testing
- Tests for the api are written with pytest, and can be run with the `pytest` command in root folder.

## License
© 2024 Henry Oberholtzer
All original code licensed under a GNU GPLv3 license.
