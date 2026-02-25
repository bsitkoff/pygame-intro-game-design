## File Structure

> 📹 **Watch:** Tour of a PyGame Zero File
> *Record in Screencastify — walkthrough of explore.py: draw(), update(), images folder*
> *Objective: I can identify what draw(), update(), and the images folder each do.*
> **[ADD VIDEO URL WHEN RECORDED]**

---

Every PyGame Zero project has the same basic shape. Here's what's in this one:

**`explore.py`** — the main game file. All your code goes here.

**`images/`** — sprites live here. The filename (without `.png`) is the Actor name. So `images/happy.png` becomes `Actor('happy')`.

---

Open `explore.py` and find these three sections:

### 1. Actors (top of file)
These are created once when the game starts. Each one has a position (`.pos`) you can change.

### 2. `draw()`
Called 60 times per second. Its job: draw everything on screen. Nothing here should change game state.

### 3. `update()`
Also called 60 times per second. Its job: move things, check collisions, respond to keyboard input.

---

> *[TODO: Add annotation or callout boxes pointing to each section in the code]*
