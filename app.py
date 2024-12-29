from flask import Flask, request, render_template_string, url_for, redirect
from live import welcome, load_game
import mysql.connector
from mysql.connector import Error
from os import getenv
from games.Web.memory_game import WebMemoryGame
import hvac

app = Flask(__name__)  # Corrected __name__ usage
print("Available routes:")
for rule in app.url_map.iter_rules():
    print(f"{rule.endpoint}: {rule.rule}")
game_instance = None

# Vault configuration
VAULT_ADDR = getenv("VAULT_ADDR", "http://vault.dvir-app.svc.cluster.local:8200")
VAULT_ROLE = getenv("VAULT_ROLE", "webapp")
JWT_PATH = getenv("JWT_PATH", "/var/run/secrets/kubernetes.io/serviceaccount/token")


def get_vault_client():
    # Create a Vault client
    client = hvac.Client(url=VAULT_ADDR)

    # Read the JWT token for Kubernetes authentication
    with open(JWT_PATH, 'r') as f:
        jwt = f.read()

    # Authenticate with Kubernetes using the client
    client.auth.kubernetes.login(role=VAULT_ROLE, jwt=jwt)

    return client


def get_db_config():
    # Create a Vault client and read the database credentials
    client = get_vault_client()

    secret_path = 'webapp/config'
    secret = client.secrets.kv.v2.read_secret_version(path=secret_path)
    username = secret['data']['data']['username']
    password = secret['data']['data']['password']

    # Return the database configuration
    return {
        'host': getenv("MYSQL_HOST", "my-app-dev-mysql.dvir-app.svc.cluster.local"),
        'user': username,
        'password': password,
        'database': 'sys',  # Use the 'sys' database
        'port': int(getenv("MYSQL_PORT", "3306")),
    }


def check_db_connection():
    try:
        # Get the database configuration from Vault
        db_config = get_db_config()

        # Use db_config directly, which now includes the credentials from Vault
        conn = mysql.connector.connect(**db_config)
        if conn.is_connected():
            return True
        else:
            return False
    except mysql.connector.Error as e:
        print(f"Error connecting to the database: {e}")
        return False
    finally:
        if 'conn' in locals() and conn.is_connected():
            conn.close()


@app.route('/test_db_connection')
def test_db_connection():
    if check_db_connection():
        return "Database connection successful", 200
    else:
        return "Failed to connect to the database", 500

def init_db():
    conn = None  # Initialize conn to None
    cursor = None  # Initialize cursor to None
    try:
        # Connect using db_config, which specifies 'sys' database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Create players table in 'sys' database
        print("Attempting to create 'players' table in 'sys' database...")
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS players (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        print("Players table created successfully or already exists in 'sys' database.")
        return True
    except mysql.connector.Error as e:
        print(f"Error initializing database: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()

# Create new connection to the 'sys' database
def get_db_connection():
    # Since db_config already includes 'database': 'sys', we can use it directly
    return mysql.connector.connect(**db_config)

# Add player to the table
def add_player(name):
    conn = None  # Initialize conn to None
    cursor = None  # Initialize cursor to None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO players (name) VALUES (%s)"
        cursor.execute(query, (name,))
        conn.commit()
        print(f"Player '{name}' added successfully to 'sys' database.")
        return True
    except mysql.connector.Error as e:
        print(f"Error adding player: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()

# List all the players
@app.route('/players')
def list_players():
    conn = None  # Initialize conn to None
    cursor = None  # Initialize cursor to None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT name, timestamp FROM players ORDER BY timestamp DESC")
        players = cursor.fetchall()
        player_list = "<h2>Player List</h2><ul>"
        for player in players:
            player_list += f"<li>{player[0]} - {player[1]}</li>"
        player_list += "</ul>"
        return player_list
    except mysql.connector.Error as e:
        return f"Error: {e}", 500
    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()

# The index.html the default of the app
@app.route('/')
def index():
    return "Welcome to the World of Games!!!!! (WoG). <a href='/welcome'>Start</a>"

@app.route('/welcome', methods=['GET', 'POST'])
def welcome_page():
    if request.method == 'POST':
        name = request.form['name']
        add_player(name)  # Save the player's name to the database
        welcome_message = welcome()
        personalized_message = f"Hello {name}! {welcome_message}"
        return f"{personalized_message}<br><a href='/game'>Choose a game</a>"
    return '''
    <form method="post">
        <label for="name">What is your name?</label>
        <input type="text" id="name" name="name" required>
        <button type="submit">Submit</button>
    </form>
    '''


@app.route('/game', methods=['GET', 'POST'])
def game_page():
    if request.method == 'POST':
        game = int(request.form['game'])
        difficulty = int(request.form['difficulty'])

        if game == 1:  # Memory Game
            return redirect(url_for('play_memory_game', difficulty=difficulty))
        # Additional games will be added later
        return f"You chose game {game} with difficulty {difficulty}"

# The main block for the code
if __name__ == '__main__':  # Corrected __name__ usage
    if check_db_connection():
        print("Database connection to 'sys' successful.")
        if init_db():
            print("Players table initialized successfully in 'sys' database.")
        else:
            print("Failed to initialize players table in 'sys' database.")
    else:
        print("Failed to connect to the 'sys' database. Please check your configuration.")

    app.run(debug=True, host='0.0.0.0')  # Added host parameter to run on all interfaces
    #tstfdssgf