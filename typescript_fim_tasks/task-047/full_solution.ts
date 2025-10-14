export interface FetchLikeResponse {
  ok: boolean;
}

export async function fetchWithFallback(
  urls: string[],
  fetcher: (url: string) => Promise<FetchLikeResponse>,
): Promise<FetchLikeResponse> {
  if (urls.length === 0) {
    throw new Error('No URLs provided');
  }

  let lastError: unknown;
  for (const url of urls) {
    try {
      const response = await fetcher(url);
      if (response.ok) {
        return response;
      }
      lastError = new Error(`Request to ${url} failed`);
    } catch (error) {
      lastError = error;
    }
  }

  throw lastError instanceof Error ? lastError : new Error('All fetch attempts failed');
}
