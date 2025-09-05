# weeklies# Weekly Music Discovery

A Python script that generates weekly music recommendations based on your Last.fm listening history. The script finds similar tracks to what you've been listening to recently but that you haven't heard before.

## Features

- Fetches your weekly listening history from Last.fm
- Finds similar tracks using the Last.fm API
- Filters out songs you've already listened to
- Saves a weekly list of music suggestions
- Can be run manually or automatically via GitHub Actions

## Prerequisites

- Python 3.11 or higher
- A Last.fm API key
- A Last.fm account with scrobbling history

## Setup

1. Clone this repository
   ```bash
   git clone https://github.com/yourusername/weekly-music-suggestions.git
   cd weekly-music-suggestions
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   (Note: The requirements file needs to be created with `python-dotenv` and `requests`)

3. Create a `.env` file in the project root with your Last.fm credentials:
   ```
   LASTFM_API_KEY=your_api_key_here
   LASTFM_USERNAME=your_username_here
   MAX_SUGGESTIONS=20  # Optional: maximum number of suggestions to generate
   ```

## Usage

Run the script manually:
```bash
python script.py
```

This will generate a file named `suggestions_YYYY-MM-DD.txt` containing your personalized music recommendations.

## GitHub Actions

The repository includes a GitHub Actions workflow that runs the script automatically every Monday at 05:00 UTC. The results are automatically committed to the repository.

To set this up:

1. Fork this repository
2. Add your Last.fm API key and username as repository secrets:
   - Go to your repository Settings > Secrets and variables > Actions
   - Add a new repository secret named `LASTFM_API_KEY` with your API key
   - Add a new repository secret named `LASTFM_USERNAME` with your Last.fm username

## How It Works

1. The script fetches your weekly listening history from Last.fm
2. For each track, it finds similar tracks using the Last.fm API
3. It filters out any tracks you've already listened to
4. It randomly selects up to `MAX_SUGGESTIONS` tracks from the results
5. The suggestions are saved to a dated text file

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
