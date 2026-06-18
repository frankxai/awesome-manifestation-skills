---
name: vibe-align
description: Turn a goal-state into a concrete music prompt — tempo, mode, instrumentation, lyric theme, and optional frequency — using the Vibe OS model, so the user can generate a track (Suno/Udio) that sets the state their work needs. Use when the user wants music to focus, get energized, feel confident, calm down, or "align" with a goal before working.
license: CC0 — see repository LICENSE
---

# Vibe Align

Translate a desired state into a ready-to-use music-generation prompt. The grounded idea: tempo controls energy (arousal), mode controls mood (valence), and lyrics carry the message. This is the deliberate, repeatable version of "set the vibe" — based on music psychology, not magic.

## When to use

The user wants a track to focus, energize, build confidence, calm down, or get into the right state for a specific task or goal.

## The model

| Dial | Controls | Range / choices |
|------|----------|-----------------|
| Tempo (BPM) | Energy / arousal | 40–60 deep calm · 60–90 relaxed focus · 90–115 creative flow · 115–135 drive · 135+ peak energy |
| Mode | Mood / valence | Major = bright, hopeful, confident · Minor = introspective, processing |
| Instruments | Texture | piano/strings = warmth · ambient pads = spaciousness · driving drums/bass = momentum · acoustic = personal |
| Lyric theme | Message underneath | affirmation · empowerment · gratitude · focus · or instrumental (no lyrics) for deep work |
| Frequency (optional) | Entrainment | theta ~6 Hz (deep focus/meditation) · alpha ~10 Hz (calm focus) · beta ~18 Hz (alertness) — held as a soft add-on, evidence is mixed |

## Steps

1. **Name the state and the task.** Ask what state the work needs ("focused calm for writing", "bold energy to ship") and roughly how long the block is.
2. **Pick the dials.** Map state → tempo, mode, instruments, lyric theme using the table. If the user is in a *different* state now (e.g. anxious), apply the ISO principle: start nearer their current state, then move toward the target across the track.
3. **Write the prompt.** Produce a clean Suno/Udio-style prompt: a style/genre line, the BPM, the mode/key feel, the instrumentation, and either a lyric direction or "[instrumental]".
4. **Add usage.** Tell them to start the track at the top of the work block and let it run — the point is to begin the work inside the state, not to listen passively.

## Output

A copy-paste music prompt plus a one-line "why these dials" and the optional frequency suggestion. Reference [Vibe OS](https://github.com/frankxai/vibe-os) for the full state library.

## Boundaries

- Frequencies/binaural claims are a soft add-on; don't oversell them. The reliable levers are tempo, mode, and lyric.
- Keep it about state for *doing the work* — not as a substitute for the action itself.
