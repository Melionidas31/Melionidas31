# VO script: portfolio motion (60 s, 1:1)

Model target: **Eleven v4** (Text to Speech).

## How this script uses Eleven v4

- **Inline audio tags** in `[square brackets]` direct the delivery: free-form directions (`[calm, measured]`), pauses (`[pause]`, `[long pause]`), and breaths (`[exhales]`). Tags are kept sparse on purpose: this is a professional narration, not a drama read.
- **No SSML.** `<break>` does not work in v4; pauses are written as `[pause]` tags instead.
- **Numbers and acronyms are spelled out** the way they should be spoken, so the model never guesses ("1.82 m" → "one point eight two metres").
- **One block per generation.** The whole script fits well under the 10,000-character limit, so generate each language in one go. The voice then stays consistent from start to end.
- **Indonesian** is supported natively by v4, so there is no need to change the voice or model for the Indonesian version.

## Recommended settings

| Setting | Value | Why |
|---|---|---|
| Model | Eleven v4 (not Turbo) | Turbo trades expressiveness for latency; a pre-rendered VO doesn't need low latency |
| Voice | Your own Professional Voice Clone, or a calm documentary narrator voice | For LinkedIn, your own voice is the most personal choice |
| Stability | Middle of the range, around "Natural" | Lower is more expressive but varies more per take; too high sounds flat |
| Output | MP3 44.1 kHz or WAV | Send me the file and I'll re-time the video to its pauses |

Generate 2–3 takes and pick the one whose pauses land most naturally. Don't edit the audio by hand: I sync the video to the real pauses.

---

## 🇬🇧 English (≈ 145 words, ≈ 58 s)

```text
[calm, measured documentary narration, confident but understated]
In process safety, every review starts with one question. [pause] How can this fail?

[long pause]

Machine learning is now entering industrial operations. [pause] Yet most models report a prediction... [pause] not how far it can be trusted.

[slightly warmer] I build models that answer both.

[pause]

My M-L surrogate replaces ALOHA dispersion simulations for real-time hazard-zone prediction. [pause] Trained on one thousand two hundred fifteen scenarios, it reduced Red-Zone error from twenty-two point two five metres... [pause] to one point eight two. [pause] And it maps where its predictions stop being reliable.

[pause]

AntiDeadline dot A-I applies the same discipline to documents: a three-stage L-L-M pipeline that turns raw files into root-cause analysis, [pause] separating verified evidence from assumptions.

In the field, an automated inspection workflow converts voice notes and photos into structured reports.

[pause]

The methods are peer-reviewed, with publications on human error probability and energy-transition policy.

[long pause]

[sincere, slower] I'm Zaki Ramdhan. [pause] A mechanical engineer, building machine learning systems that know their limits.
```

## 🇮🇩 Bahasa Indonesia (≈ 125 kata, ≈ 60 dtk)

Istilah teknis yang lazim dipakai engineer Indonesia (machine learning, surrogate model, pipeline, root cause analysis) sengaja tidak diterjemahkan.

```text
[narasi dokumenter yang tenang dan terukur, percaya diri tapi tidak berlebihan]
Dalam process safety, setiap kajian dimulai dengan satu pertanyaan. [pause] Bagaimana sistem ini bisa gagal?

[long pause]

Kini machine learning mulai masuk ke operasi industri. [pause] Namun sebagian besar model hanya memberi prediksi... [pause] bukan seberapa jauh prediksi itu bisa dipercaya.

[sedikit lebih hangat] Saya membangun model yang menjawab keduanya.

[pause]

Surrogate model saya menggantikan simulasi dispersi ALOHA untuk memprediksi zona bahaya secara real-time. [pause] Dilatih dengan seribu dua ratus lima belas skenario, error Zona Merah turun dari dua puluh dua koma dua lima meter... [pause] menjadi satu koma delapan dua meter. [pause] Model ini juga memetakan kapan prediksinya tidak lagi bisa diandalkan.

[pause]

AntiDeadline dot A-I menerapkan disiplin yang sama pada dokumen: pipeline L-L-M tiga tahap yang mengubah dokumen mentah menjadi root cause analysis, [pause] dengan bukti terverifikasi yang dipisahkan dari asumsi.

Di lapangan, alur inspeksi otomatis mengubah voice note dan foto menjadi laporan terstruktur.

[pause]

Metode-metode ini telah melalui peer review, dengan publikasi tentang probabilitas human error dan kebijakan transisi energi.

[long pause]

[tulus, lebih pelan] Saya Zaki Ramdhan. [pause] Seorang mechanical engineer yang membangun sistem machine learning yang tahu batas kemampuannya.
```

---

## Timing map (video ↔ VO)

| Detik | Babak | EN | ID |
|---|---|---|---|
| 0–7 | 1. Asal (FMEA) | "In process safety… How can this fail?" | "Dalam process safety… bisa gagal?" |
| 7–15 | 2. Masalah | "Machine learning… can be trusted." | "Kini machine learning… bisa dipercaya." |
| 15–18 | 3. Pendekatan | "I build models that answer both." | "Saya membangun model…" |
| 18–30 | 4. ALOHA surrogate | "My ML surrogate… stop being reliable." | "Surrogate model saya… bisa diandalkan." |
| 30–41 | 5. AntiDeadline.ai | "AntiDeadline dot AI… from assumptions." | "AntiDeadline dot A-I… dari asumsi." |
| 41–48 | 6. Field inspection | "In the field… structured reports." | "Di lapangan… laporan terstruktur." |
| 48–54 | 7. Publikasi | "The methods are peer-reviewed…" | "Metode-metode ini…" |
| 54–60 | 8. Penutup | "I'm Zaki Ramdhan…" | "Saya Zaki Ramdhan…" |

These timings are estimates. Once the audio is in, the video is re-timed to the real pauses. On-screen text stays in English for both versions unless requested otherwise, so one video can carry either VO; an Indonesian on-screen variant can be built on request.
