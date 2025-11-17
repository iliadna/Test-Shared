def build_url(base: str, endpoint: str, **params) -> str:
    query = "&".join(f"{k}={v}" for k, v in params.items())
    return f"{base}/{endpoint}?{query}" if params else f"{base}/{endpoint}"


def validate_ip(ip: str) -> bool:
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    try:
        return all(0 <= int(p) <= 255 for p in parts)
    except ValueError:
        return False


def ping_host(host: str) -> str:
    return f"Pinging {host}... (simulated)"
