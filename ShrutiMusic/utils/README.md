**Utils Directory**

Shared helpers powering the rest of the codebase. Anything that's not a command handler or a client wrapper lives here.

---

**Top-Level Modules**

| File | Purpose |
|------|---------|
| `channelplay.py` | Resolve linked-channel logic for `/cplay` |
| `couple.py` | Daily couple-of-the-day picker with persistent cache |
| `error.py` | Global Pyrogram exception handler — logs tracebacks |
| `exceptions.py` | Custom exception classes raised across the codebase |
| `extraction.py` | Extract user / chat / reason from command arguments |
| `formatters.py` | Time, size, and number formatters used by the UI |
| `functions.py` | Misc helpers — admin check, time conversion, etc. |
| `inlinequery.py` | Inline-mode answer builder |
| `keyboard.py` | Static inline keyboard factories |
| `logger.py` | Forward important events to the log group |
| `pastebin.py` | Upload long text to a paste service |
| `permissions.py` | Cached chat-admin lookups |
| `sys.py` | System info — CPU, RAM, disk, uptime |
| `thumbnails.py` | Generate now-playing thumbnails using Pillow |

---

**Sub-packages**

| Folder | Purpose |
|--------|---------|
| `database/` | DB layer — Mongo, in-memory, assistant tracking |
| `decorators/` | Function decorators for permissions & language |
| `inline/` | Inline-keyboard builders, organised by feature |
| `stream/` | Voice-chat stream lifecycle, queue, autoclear |

---

**Design Principles**

- Small, focused modules — easy to test, easy to reuse
- Async-first; no blocking I/O on the event loop
- All persistent state goes through `database/`
- All user-visible strings go through `strings/`
