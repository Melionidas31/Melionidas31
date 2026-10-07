# Portfolio motion — "Models that know their limits"

A 69-second, 1:1 (1080×1080) motion piece for LinkedIn, built with the
[Bang Motion](https://github.com/bangtutorial/bang-motion) skill as a single HTML
page that plays like a video.

| File | What it is |
|---|---|
| `portfolio-motion.mp4` | Final render: 1080×1080, 60 fps, H.264 + AAC (VO + ambient music) |
| `thumbnail.png` | Closing frame, for LinkedIn's custom thumbnail |
| `index.html` | The animation itself. Double-click to play (autoplay, loop, no player) |
| `vo-script.md` | EN + ID voice-over scripts written for ElevenLabs Eleven v4 |
| `assets/vo-en.mp3` | English VO (ElevenLabs Eleven v4, voice clone) |
| `assets/soundtrack.mp3` | VO mixed with the ambient bed (music ducks under the voice), −16 LUFS |
| `assets/img/` | Project screenshots from the portfolio repo; names, locations and site photos are blurred |
| `tools/make_music.py` | Generates the ambient music bed (numpy only, deterministic) |
| `tools/render.mjs`, `tools/snap.mjs` | Frame-by-frame MP4 render and key-frame snapshots (Node + puppeteer-core; set `CHROME` to your Chrome path) |

## Viewing

- Open `index.html` in a browser. If the browser blocks autoplay with sound, it waits on the first frame and starts on the first click.
- `index.html?debug=1` shows a scrub bar. `R` restarts, `Space` pauses.
- Everything (fonts, GSAP, images, audio) is local, so it also works offline.

## Structure

One continuous engineering drawing sheet. Each part of the story is a numbered zone on the sheet, linked by
process-flow arrows. The camera travels between zones, and near the end it pulls back to show the whole sheet.

| Time | Zone | VO |
|---|---|---|
| 0:00 | 01 FMEA | In process safety… how can this fail? |
| 0:06 | 02 Prediction ≠ trust | Machine learning… how far it can be trusted |
| 0:16 | 01+02 | I build models that answer both |
| 0:18 | 03 ALOHA hazard map | My ML surrogate replaces ALOHA… |
| 0:24 | 04 1,215 scenarios → 22.25 → 1.82 m → trusted range | Trained on… stop being reliable |
| 0:36 | 05 AntiDeadline.ai | Three-stage LLM pipeline… evidence vs assumptions |
| 0:48 | 06 Field inspection bot | Voice notes and photos → structured reports |
| 0:54 | 07 Publications | Peer-reviewed |
| 1:00 | whole sheet → 08 close | I'm Zaki Ramdhan… |

## Swapping the audio (e.g. the Indonesian VO)

The timeline is keyed to the pauses in `assets/vo-en.mp3`. A new VO needs its scene times re-mapped to the
new pauses (`ffmpeg -i vo.mp3 -af silencedetect=noise=-35dB:d=0.25 -f null -`), then the soundtrack is
re-mixed:

```bash
python3 tools/make_music.py music.wav
ffmpeg -i assets/vo-en.mp3 -i music.wav -filter_complex "[0:a]aformat=sample_rates=44100:channel_layouts=stereo,apad=whole_dur=69,asplit=2[vo][sc];[1:a]volume=0.13[mu];[mu][sc]sidechaincompress=threshold=0.03:ratio=5:attack=40:release=500[duck];[vo][duck]amix=inputs=2:normalize=0:duration=first,loudnorm=I=-16:TP=-1.5:LRA=11" -t 69 -c:a libmp3lame -b:a 192k assets/soundtrack.mp3
```
