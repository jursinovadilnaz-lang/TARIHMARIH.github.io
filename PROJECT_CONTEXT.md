# TARX (Kazakhstan Interactive History Game) - Project Context

This document is for AI assistants to quickly understand the project state, goals, and user preferences.

## 🎯 Project Objective
**TARX** is an interactive, web-based educational game about the history of Kazakhstan. It aims to teach students (4-8 grades) through engaging "mini-quests" rather than simple text or quizzes.

## 🛠 Tech Stack
- **Frontend:** Vanilla HTML5, CSS3, JavaScript.
- **Styling:** Premium aesthetic, dark theme, gold accents (`#D4AF37`), Cinzel/Montserrat fonts, complex CSS animations.
- **Assets:** AI-generated photorealistic images for landscapes, SVG/Emoji for items.

## 📂 Current Progress & File Structure

### 1. `index.html` (Landing Page)
- **Title Animation:** A sophisticated "decoding" effect for the word **"ТАРИХ"**. Characters cycle through Roman-like symbols for 5 seconds before sequentially locking into final letters.
- **Sound Effect:** A playful female giggle (Web Audio API) plays when the "Бастау" (Start) button is clicked.
- **Visuals:** Animated gold particles, rotating ornaments, and glowing stars behind the main card. Hover effect on the button includes a white ripple/wave.
- **Design:** Radial glow background, premium card layout with glassmorphism.

### 2. `level.html` (First Level: Stone Age)
Contains 3 interactive tasks:
- **Task 1: Gathering (Тірі Қалу Жолы):** Drag/click logic to pick 3 essential survival items. Uses 3D-style CSS items with bounce animations.
- **Task 2: Fire Making (Отты Сақта):** 
    - **Phase 1:** Strike stones (drag logic) to generate sparks and heat.
    - **Phase 2:** Once at 50% heat, use a leaf fan (click logic) to maintain and grow the flame.
    - **Fixed Gameplay:** Heat decay is slow, and there is a 300ms cooldown between stone strikes to prevent instant winning.
- **Task 3: Settlement Choice (Қоныс Таңдау):**
    - **Visuals:** Winter-processed photorealistic images (`winter_river.png`, `winter_mountain_cave.png`, `winter_steppe.png`).
    - **Winter Effect:** Python script applies +20% brightness, +15% contrast, and blue tint for sunny winter day atmosphere.
    - **CSS Filters:** Additional brightness (1.15), contrast (1.1), and cool blue gradient overlay.
    - **Layout:** Three cards (250px × 320px) in a single row with 25px gap.
    - **Logic:** Information boxes explain each choice. Selecting the Cave is the "Correct" path for winter survival.

### 3. `level.html` (Second Level: Bronze Age & Early Nomads)
Contains 3 interactive tasks:
- **Task 1: Bronze Smelting (Қола Балқыту):**
    - **Mechanics:** Adjust two sliders to mix copper (90%) and tin (10%) in correct ratio.
    - **Visuals:** Animated furnace with glowing fire, slider controls, result feedback.
    - **Logic:** Validates ratio with 5% tolerance, shows success/failure message.
- **Task 2: Herd Management (Мал Үйірін Жинау):**
    - **Mechanics:** Select 10 animals using +/- buttons (3 horses, 4 sheep, 2 camels, 1 cow).
    - **Visuals:** Animal cards with emoji icons, counters, status display.
    - **Logic:** Checks exact distribution, auto-resets on wrong combination.
- **Task 3: Petroglyph Matching (Петроглиф Сәйкестендіру):**
    - **Mechanics:** Click-to-match 6 ancient symbols with their meanings.
    - **Visuals:** Two-column grid, selection highlighting, checkmarks on matches.
    - **Logic:** Validates matches, shows visual feedback, completes when all matched.

### 4. `game.html` (Placeholder / Map)
- Intended to be the level selection map (currently linked from `level.html` and `index.html`).

## ✨ User Preferences & Style Guide
- **Language:** Kazakh (KK).
- **Aesthetics:** "Wowed at first glance". No placeholders. Everything must look "Premium".
- **Interactivity:** Every button should have a hover/active state and preferably a sound.
- **Short & Sweet:** Descriptions should be poetic and rhythmic (e.g., "7 дәуір. 7 тапсырма. Бір ұлы саяхат.").

## 🚀 Recent Requests & Feedback
- The user prefers realistic graphics for landscapes (used `generate_image`).
- Fixed a bug in the fire-making game where heat increased too fast.
- **Winter Images (2026-02-05):**
  - Created Python script (`create_winter_images.py`) to process existing images with winter effects.
  - Applied brightness (+20%), contrast (+15%), and blue tint to create sunny winter day atmosphere.
  - Replaced falling snow animation with CSS filters and gradient overlay.
  - All three location images now show winter scenes with consistent sizing (250px × 320px).
- **Level 2: Bronze Age (2026-02-05):**
  - Implemented three interactive tasks: Bronze Smelting, Herd Management, Petroglyph Matching.
  - Added 283 lines of CSS for furnace animation, animal cards, and matching grid.
  - Added 159 lines of JavaScript for game logic and validation.
  - All tasks feature smooth animations, visual feedback, and age-appropriate difficulty.
- Title animation timing: ~5 seconds total for reveal.
- Button sound: Must be a female voice/giggle.

---
*Last Updated: 2026-02-05*
