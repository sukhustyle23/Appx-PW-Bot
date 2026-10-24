import os

api_id = int(os.environ.get("API_ID", 34262281))
api_hash = os.environ.get("API_HASH", "1ac11b5ecb8a078dd703fbaa81ca7c1b")
bot_token = os.environ.get("BOT_TOKEN", "8803357104:AAHOhYEIjm1ec_TmvYwIu0BntZOATFEvWxs")
auth_users = [int(x.strip()) for x in os.environ.get("AUTH_USERS", "1659977801").split(",") if x.strip().isdigit()]

if not api_id: raise ValueError("Set API_ID env var!")
if not api_hash: raise ValueError("Set API_HASH env var!")
if not bot_token: raise ValueError("Set BOT_TOKEN env var!")
if not auth_users: raise ValueError("Set AUTH_USERS env var!")
