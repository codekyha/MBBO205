"""Ollama REST API için küçük istemci (yalnızca `requests` gerektirir)."""
import json, os, time, requests
HOST = os.environ.get("OLLAMA_HOST", "http://localhost:11434")

def hazir() -> bool:
    try: return requests.get(f"{HOST}/api/tags", timeout=3).status_code == 200
    except requests.RequestException: return False

def uret(model: str, istem: str, sistem: str = "", sicaklik: float = 0.2, num_ctx: int = 4096, akis: bool = False, json_mod: bool = False):
    govde = {"model": model, "prompt": istem, "system": sistem, "stream": akis, "options": {"temperature": sicaklik, "num_ctx": num_ctx}}
    if json_mod: govde["format"] = "json"
    t = time.perf_counter()
    if not akis:
        r = requests.post(f"{HOST}/api/generate", json=govde, timeout=600).json()
        sure = time.perf_counter() - t
        return r["response"], {"token": r.get("eval_count", 0), "token_s": r.get("eval_count", 0) / max(r.get("eval_duration", 1) / 1e9, 1e-9), "sure": sure}
    parcalar = []
    with requests.post(f"{HOST}/api/generate", json=govde, stream=True, timeout=600) as r:
        for satir in r.iter_lines():
            if satir:
                j = json.loads(satir); parcalar.append(j.get("response", "")); print(j.get("response", ""), end="", flush=True)
    print(); return "".join(parcalar), {"sure": time.perf_counter() - t}

def sohbet(model: str, mesajlar: list[dict], sicaklik: float = 0.2) -> str:
    r = requests.post(f"{HOST}/api/chat", json={"model": model, "messages": mesajlar, "stream": False, "options": {"temperature": sicaklik}}, timeout=600).json()
    return r["message"]["content"]
