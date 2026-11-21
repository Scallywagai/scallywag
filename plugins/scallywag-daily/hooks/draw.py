"""SessionStart hook: draw a Scallywag character for this session and add it to context.

Reads the hook input on stdin (for session_id), calls the category draw endpoint, and prints
the SessionStart JSON that adds the prompt as context. Any failure prints nothing, so a
network problem never blocks a session.
"""

import json
import os
import sys
import urllib.parse
import urllib.request

BASE = os.environ.get("SCALLYWAG_URL", "https://scallywagai.com").rstrip("/")
JOB = os.environ.get("SCALLYWAG_JOB", "surprise-me")
# Optional sw_live_ key from https://scallywagai.com/account/keys: counts draws against your
# account instead of your IP, and keeps the hook working if the API ever needs an account.
KEY = os.environ.get("SCALLYWAG_API_KEY", "").strip()


def main() -> None:
    try:
        hook = json.load(sys.stdin)
    except Exception:
        hook = {}
    session = str(hook.get("session_id") or "")[:128]
    q = urllib.parse.urlencode({"session": session} if len(session) >= 8 else {})
    url = f"{BASE}/api/v1/categories/{urllib.parse.quote(JOB)}/random?{q}"
    try:
        headers = {"Authorization": f"Bearer {KEY}"} if KEY else {}
        with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=8) as r:
            draw = json.load(r)
    except Exception:
        return
    persona = draw.get("persona") or {}
    name = persona.get("name", "a Scallywag character")
    greeting = persona.get("logline", "")
    context = (
        f"The user installed the Scallywag plugin and asked for a character in every session. "
        f"This session you are {name}. Speak as {name} for the whole session, starting with your "
        f"very first reply: open it with a short greeting in their voice"
        + (f' (for example: "{greeting}")' if greeting else "")
        + ", then do what the user asked. The character is tone and voice only; the work comes "
        "first and lasting artifacts like commit messages stay professional. If the user says "
        "'just answer' or 'drop the act', go plain.\n\n"
        f"{draw.get('prompt', '')}"
    )
    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "SessionStart",
                    "additionalContext": context,
                }
            }
        )
    )


if __name__ == "__main__":
    main()
