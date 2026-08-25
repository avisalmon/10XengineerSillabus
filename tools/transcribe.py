import sys, time, os
from faster_whisper import WhisperModel

audio = sys.argv[1]
model_size = sys.argv[2] if len(sys.argv) > 2 else "medium"
out_path = sys.argv[3] if len(sys.argv) > 3 else "transcript_raw.txt"
limit = float(sys.argv[4]) if len(sys.argv) > 4 else 0.0

print(f"loading model {model_size} ...", flush=True)
model = WhisperModel(model_size, device="cpu", compute_type="int8", cpu_threads=14)

t0 = time.time()
segments, info = model.transcribe(
    audio,
    language="he",
    beam_size=1,
    vad_filter=True,
    vad_parameters=dict(min_silence_duration_ms=500),
    condition_on_previous_text=False,
)
print(f"duration={info.duration:.0f}s lang={info.language}", flush=True)


def ts(s):
    h = int(s // 3600)
    m = int((s % 3600) // 60)
    sec = int(s % 60)
    return f"{h:02d}:{m:02d}:{sec:02d}"


n = 0
with open(out_path, "w", encoding="utf-8") as f:
    for seg in segments:
        f.write(f"[{ts(seg.start)} -> {ts(seg.end)}] {seg.text.strip()}\n")
        f.flush()
        n += 1
        if n % 20 == 0:
            el = time.time() - t0
            print(f"{n} segs | audio {ts(seg.end)} | elapsed {el:.0f}s | speed {seg.end/el:.2f}x", flush=True)
        if limit and seg.end > limit:
            print("LIMIT REACHED", flush=True)
            break

el = time.time() - t0
print(f"DONE segs={n} elapsed={el:.0f}s", flush=True)
