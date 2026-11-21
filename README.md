# Scallywag

Personalities for your coding agent, from [scallywagai.com](https://scallywagai.com): a stern reviewer, a calm incident lead, a theatrical tutor and more. A character changes how your agent talks, never what it's allowed to do.

This repo holds the plugins and setup for agent tools. The characters themselves live on the site; the plugins fetch them when they run.

## Claude Code

```
/plugin marketplace add Scallywagai/scallywag
/plugin install scallywag@scallywag
```

Then ask for one: "grab a stern personality from Scallywag and review my last commit."

The plugin adds the Scallywag MCP server. The first time it's used, run `/mcp`, pick `scallywag` and authenticate: a browser opens so you can sign in (accounts are free).

### A new character every session

```
/plugin install scallywag-daily@scallywag
```

Draws a character at the start of every session. Set these in your environment if you like:

| Variable            | What it does                                                                                                                                      |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `SCALLYWAG_JOB`     | Draw for a job: `code`, `ops`, `research`, `learn`, `write`, `data`, `assistant`, `ideas`, `coach`. Default `surprise-me`.                          |
| `SCALLYWAG_API_KEY` | A key from [your account](https://scallywagai.com/account/keys), so draws count against your account's limits instead of your IP. |

If Scallywag can't be reached, the session starts as normal, without a character.

## Other tools

Scallywag is an MCP server at `https://scallywagai.com/mcp`. The first connection opens a browser to sign in.

| Tool       | Setup                                                                               |
| ---------- | ----------------------------------------------------------------------------------- |
| Codex      | `codex mcp add scallywag --url https://scallywagai.com/mcp`                         |
| Cursor     | In `~/.cursor/mcp.json`: `{ "mcpServers": { "scallywag": { "url": "https://scallywagai.com/mcp" } } }` |
| VS Code    | `code --add-mcp '{"name":"scallywag","type":"http","url":"https://scallywagai.com/mcp"}'` |
| Gemini CLI | `gemini mcp add --transport http scallywag https://scallywagai.com/mcp`             |

Tools that can't sign in can use an API key instead; see [the developer docs](https://scallywagai.com/developers).

## Problems

Open an [issue](https://github.com/Scallywagai/scallywag/issues).
