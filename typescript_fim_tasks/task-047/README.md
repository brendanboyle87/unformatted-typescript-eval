# Description

- **Domain:** async
- Write `fetchWithFallback(urls: string[], fetcher: (url: string) => Promise<{ ok: boolean }>): Promise<{ ok: boolean }>`.
- Try each URL in order until `ok` is true; otherwise reject with the last error encountered.
