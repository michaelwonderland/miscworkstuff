"""Minimal Apify client: start actor runs in parallel, wait, fetch dataset items."""
import json
import os
import time
import urllib.request

API = "https://api.apify.com/v2"
TOKEN = os.environ["APIFY_TOKEN"]


def _req(method, path, body=None):
    req = urllib.request.Request(
        API + path,
        method=method,
        data=json.dumps(body).encode() if body is not None else None,
        headers={"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read())


def start(actor, run_input, memory_mb=1024):
    return _req("POST", f"/acts/{actor.replace('/', '~')}/runs?memory={memory_mb}", run_input)["data"]


def wait(run_ids, poll=15, timeout=3600):
    """Block until all runs finish. Returns {run_id: run_data}."""
    done, t0 = {}, time.time()
    while len(done) < len(run_ids) and time.time() - t0 < timeout:
        for rid in run_ids:
            if rid in done:
                continue
            d = _req("GET", f"/actor-runs/{rid}")["data"]
            if d["status"] in ("SUCCEEDED", "FAILED", "ABORTED", "TIMED-OUT"):
                done[rid] = d
        if len(done) < len(run_ids):
            print(f"  {len(done)}/{len(run_ids)} runs finished...", flush=True)
            time.sleep(poll)
    return done


def items(dataset_id):
    out, offset = [], 0
    while True:
        batch = _req("GET", f"/datasets/{dataset_id}/items?clean=true&offset={offset}&limit=1000")
        out += batch
        if len(batch) < 1000:
            return out
        offset += 1000


def run_many(actor, inputs, memory_mb=1024):
    """Run one actor over many inputs in parallel. Returns list of (input, items, run)."""
    runs = [start(actor, i, memory_mb) for i in inputs]
    finished = wait([r["id"] for r in runs])
    res = []
    for inp, r in zip(inputs, runs):
        d = finished.get(r["id"], r)
        res.append((inp, items(d["defaultDatasetId"]) if d.get("status") == "SUCCEEDED" else [], d))
    return res
