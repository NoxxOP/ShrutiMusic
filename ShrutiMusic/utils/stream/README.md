**Stream Engine**

The runtime that actually plays music. Sits on top of PyTgCalls and manages the lifecycle of every voice-chat session.

---

**Modules**

| File | Purpose |
|------|---------|
| `stream.py` | Start a new stream — resolves source, downloads/pipes media, hands it to PyTgCalls, posts the now-playing card |
| `queue.py` | In-memory per-chat queue — push, pop, clear, shuffle, loop counters |
| `autoclear.py` | Clears stale download files / cached metadata after a stream ends |

---

**Stream Lifecycle**

1. `/play` handler calls `stream(...)`
2. Source resolved via `platforms/*`
3. If queue is empty → start playback immediately; else append to queue
4. PyTgCalls events (track end, stream end) trigger the next item via `queue.py`
5. When the queue empties → `autoclear` cleans up and the assistant leaves (configurable)

---

**Notes**

- All queue state is in-memory — restarting the bot drops the queue (this is intentional)
- `autoclear` is throttled to avoid deleting files still being read by FFmpeg
- Loop logic decrements a counter inside `queue.py` until zero
