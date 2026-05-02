**ShrutiMusic Package**

The main Python package for the bot. This is the entry point that boots all clients, loads plugins, and starts the music streaming engine.

---

**Module Overview**

| File / Folder | Description |
|---------------|-------------|
| `__init__.py` | Initializes shared singletons — Bot, Userbot, PyTgCalls, MongoDB |
| `__main__.py` | The runtime entry point — `python -m ShrutiMusic` |
| `logging.py` | Centralized logger with rotating file handler and console output |
| `misc.py` | Miscellaneous globals — start time, sudoers cache, heroku app handle |
| `core/` | Client wrappers — Bot, Userbot, Call, Mongo, Git, Dir |
| `platforms/` | Music source integrations |
| `plugins/` | All command handlers, grouped by category |
| `utils/` | Helpers — database, decorators, inline UI, stream control |
| `assets/` | Static media — fonts, icons, thumbnails |

---

**Boot Sequence**

1. `__main__.py` is invoked
2. `__init__.py` instantiates Bot, Userbot, PyTgCalls, and Mongo clients
3. Plugins under `plugins/` are auto-loaded by Pyrogram
4. PyTgCalls handlers are registered
5. Bot enters polling state and is ready to serve

---

**Extending the Bot**

- Add a new command → drop a `.py` file inside the matching `plugins/` sub-folder
- Add a new music source → create a class in `platforms/` mirroring the existing pattern
- Add a new helper → place it under `utils/` and import where needed
