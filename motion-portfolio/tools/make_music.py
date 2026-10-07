"""Procedural ambient bed for the portfolio motion (deterministic, numpy only).

Soft additive pad + sub + sparse plucked arpeggio, D major colour, ~69 s.
Cues follow the edit: arpeggio enters at the first project (18 s), the bed
swells for the 22.25 -> 1.82 m moment (31.4 s), thins for the pull-back
(59.9 s) and resolves on the name (61.1 s).
"""
import sys, wave
import numpy as np

SR, DUR = 44100, 69.0
n = int(SR * DUR)
t = np.arange(n) / SR

def hz(m):  # midi -> Hz
    return 440.0 * 2 ** ((m - 69) / 12)

def env_seg(start, end, a=2.5, r=3.0):
    e = np.zeros(n)
    i0, i1 = int(start * SR), min(int((end + r) * SR), n)
    tt = t[i0:i1] - start
    up = np.clip(tt / a, 0, 1) ** 2 * (3 - 2 * np.clip(tt / a, 0, 1))
    down = np.clip(1 - (tt - (end - start)) / r, 0, 1)
    e[i0:i1] = up * down
    return e

def pad_voice(m, amp):
    f = hz(m)
    out = np.zeros(n)
    for k, g in ((1, 1.0), (2, .32), (3, .14), (4, .06)):
        for det in (-.11, .13):
            out += g * np.sin(2 * np.pi * (f * k + det * k) * t + k * 1.7 + det * 9)
    return amp * out

# chord plan (midi notes): Dmaj9, Bm9, Gmaj7(#11), Asus -> resolves to Dmaj9
plan = [
    (0.0, 9.0, [50, 57, 61, 64, 66]),
    (8.5, 18.0, [47, 54, 57, 61, 62]),
    (17.5, 26.5, [43, 50, 54, 61, 64]),
    (26.0, 33.5, [45, 52, 57, 62, 64]),
    (33.0, 42.0, [50, 57, 61, 64, 66]),
    (41.5, 50.5, [47, 54, 57, 61, 62]),
    (50.0, 59.5, [43, 50, 54, 61, 64]),
    (59.0, 61.6, [45, 52, 57, 62, 64]),
    (61.1, 69.0, [50, 57, 61, 64, 66, 69]),
]
pad = np.zeros(n); sub = np.zeros(n)
for s, e, notes in plan:
    ev = env_seg(s, e, a=2.2, r=2.6)
    for m in notes:
        pad += ev * pad_voice(m, .05)
    sub += ev * .16 * np.sin(2 * np.pi * hz(notes[0] - 12) * t)

# global dynamics: quiet intro, lift for the projects, swell at the key number, thin on pull-back
def ramp(points):
    xs, ys = zip(*points)
    return np.interp(t, xs, ys)
dyn = ramp([(0, .55), (6, .7), (17.5, .8), (19, 1.0), (30.5, 1.0), (31.4, 1.25), (34, 1.0), (59.5, 1.0), (60.2, .55), (61.1, 1.1), (66, 1.0), (69, 0.0)])
bright = ramp([(0, .0), (18, .0), (19.5, 1.0), (59.6, 1.0), (60.2, .0), (61.1, .8), (69, .6)])

# plucked arpeggio, quarter notes at 100 bpm (0.6 s), tones from the current chord
arp = np.zeros(n)
step = .6
def chord_at(x):
    cur = plan[0][2]
    for s, e, notes in plan:
        if s <= x:
            cur = notes
    return cur
pattern = [2, 3, 4, 3, 1, 3, 4, 2]
i = 0
x = 0.0
while x < DUR - .5:
    notes = chord_at(x)
    m = notes[pattern[i % len(pattern)] % len(notes)] + 12
    i0 = int(x * SR); L = min(int(2.2 * SR), n - i0)
    tt = np.arange(L) / SR
    tone = (np.sin(2 * np.pi * hz(m) * tt) + .25 * np.sin(2 * np.pi * hz(m) * 2 * tt)) * np.exp(-tt * 3.2) * (1 - np.exp(-tt * 400))
    vel = .85 if i % 4 == 0 else .6
    arp[i0:i0 + L] += vel * .07 * tone
    x += step; i += 1
arp *= bright

# a soft bell on the resolution (name)
i0 = int(61.1 * SR); L = n - i0; tt = np.arange(L) / SR
for m, g in ((74, .06), (81, .035), (86, .02)):
    arp[i0:] += g * np.sin(2 * np.pi * hz(m) * tt) * np.exp(-tt * .9)

mix = (pad + sub) * dyn + arp * np.clip(dyn, 0, 1.1)

# cheap stereo room: a few tapped delays, different per side
def taps(x, spec):
    y = x.copy()
    for d, g in spec:
        k = int(d * SR); y[k:] += g * x[:-k]
    return y
L = taps(mix, [(.137, .32), (.291, .22), (.443, .14), (.71, .08)])
R = taps(mix, [(.173, .32), (.317, .22), (.487, .14), (.66, .08)])
st = np.stack([L, R], 1)
fade = np.clip(np.minimum(t / 1.5, (DUR - t) / 2.5), 0, 1)[:, None]
st *= fade
st /= np.max(np.abs(st)) / .7
with wave.open(sys.argv[1], 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((st * 32767).astype('<i2').tobytes())
print('ok', sys.argv[1])
