## File Structure

📹 **Watch:** Tour of a PyGame Zero File

<iframe width="720" height="600"
  src="https://app.screencastify.com/watch/YvdwYgQp7r7zD8ZUpRez/embed"
  title="Codio - Intro to Game Design - Screencastify - March 15, 2026 2:36 PM"
  frameborder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
  referrerpolicy="strict-origin-when-cross-origin"
  allowfullscreen
></iframe>
  

---

Every PyGame Zero project has the same basic shape. Here's what's in this one:

**`explore.py`** — the main game file. All your code goes here.

**`images/`** — sprites live here. The filename (without `.png`) is the Actor name. So `images/happy.png` becomes `Actor('happy')`.

---

Open `explore.py` and find these three sections:

### 1. Actors (top of file)
These are created once when the game starts. Each one has a position (`.pos`) you can change.

### 2. `draw()`
Called 60 times per second. Its job: draw everything on screen. Nothing here should change game state. Look for the global variables and notice that they match the variables we defined outside the function.

### 3. `update()`
Also called 60 times per second. Its job: move things, check collisions, respond to keyboard input.

---

