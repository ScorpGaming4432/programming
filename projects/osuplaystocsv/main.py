import requests
import json
from urllib.parse import urlencode
from http.server import HTTPServer, BaseHTTPRequestHandler
from threading import Thread
import webbrowser
import time

# OAuth Configuration
OAUTH_CLIENT_ID = 60195
OAUTH_CLIENT_SECRET = "dakiPsAaSOHRTEfs61lvXyGtrMiNvQo0o57GNkzI"
OAUTH_REDIRECT_URL = "http://localhost:8000"  # Your redirect URL

# Global variable to store the authorization code
auth_code = None
server_ready = False


class OAuthCallbackHandler(BaseHTTPRequestHandler):
    """Handler for OAuth callback"""
    
    def do_GET(self):
        global auth_code
        
        # Parse the query string to get the authorization code
        if "code=" in self.path:
            auth_code = self.path.split("code=")[1].split("&")[0]
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<html><body><h1>Authorization successful!</h1><p>You can close this window.</p></body></html>")
        else:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Error: No authorization code received")
    
    def log_message(self, format, *args):
        # Suppress default logging
        pass


def start_callback_server():
    """Start a local HTTP server to handle OAuth callbacks"""
    global server_ready
    server = HTTPServer(("localhost", 8000), OAuthCallbackHandler)
    server_ready = True
    server.handle_request()  # Handle only one request then close


def get_oauth_token():
    """Get OAuth access token using Authorization Code Grant"""
    global auth_code
    
    # Step 1: Start the callback server
    server_thread = Thread(target=start_callback_server, daemon=True)
    server_thread.start()
    
    # Wait for server to be ready
    while not server_ready:
        time.sleep(0.1)
    
    # Step 2: Redirect user to OAuth authorization URL
    auth_url = "https://osu.ppy.sh/oauth/authorize?" + urlencode({
        "client_id": OAUTH_CLIENT_ID,
        "redirect_uri": OAUTH_REDIRECT_URL,
        "response_type": "code",
        "scope": "public identify"
    })
    
    print(f"Opening browser for authorization...")
    print(f"Authorization URL: {auth_url}")
    webbrowser.open(auth_url)
    
    # Wait for the callback to set auth_code
    timeout = 120
    start_time = time.time()
    while auth_code is None and (time.time() - start_time) < timeout:
        time.sleep(1)
    
    if auth_code is None:
        raise Exception("Failed to get authorization code (timeout)")
    
    print(f"Authorization code received: {auth_code[:20]}...")
    
    # Step 3: Exchange authorization code for access token
    token_response = requests.post(
        "https://osu.ppy.sh/oauth/token",
        headers={"Accept": "application/json"},
        data={
            "client_id": OAUTH_CLIENT_ID,
            "client_secret": OAUTH_CLIENT_SECRET,
            "code": auth_code,
            "grant_type": "authorization_code",
            "redirect_uri": OAUTH_REDIRECT_URL
        }
    )
    
    if token_response.status_code != 200:
        print(f"Error: {token_response.status_code}")
        print(token_response.text)
        raise Exception("Failed to get access token")
    
    token_data = token_response.json()
    access_token = token_data["access_token"]
    print(f"Access token obtained successfully!")
    
    return access_token


def get_user_scores(access_token:str, user_id:int):
    """Get user's best scores using the access token"""
    headers = {"Authorization": f"Bearer {access_token}"}

    all_maps = []
    offset = 0
    limit = 100

    while True:
        resp = requests.get(
            f"https://osu.ppy.sh/api/v2/users/{user_id}/beatmapsets/most_played",
            headers=headers,
            params={"limit": limit, "offset": offset}
        )
        batch = resp.json()
        
        if not batch:
            break
        
        all_maps.extend(batch)
        print(f"Fetched {len(all_maps)} so far...")
        offset += limit
        time.sleep(1)

    print(f"Total: {len(all_maps)} maps")
    return all_maps


# Main execution
if __name__ == "__main__":
    # Get access token using OAuth
    try:
        access_token = get_oauth_token()
        print(f"Access token: {access_token[:50]}...")
        
        # Now use the token to get user scores
        USER_ID = 23209230  # your osu! user ID
        scores = get_user_scores(access_token, USER_ID)
        
        if scores:
            print(f"\nRetrieved {len(scores)} scores")
            
            # Save scores to JSON file
            output_file = "scores.json"
            with open(output_file, "w") as f:
                json.dump(scores, f, indent=2)
            
            print(f"Scores saved to {output_file}")
        
    except Exception as e:
        print(f"Error: {e}")