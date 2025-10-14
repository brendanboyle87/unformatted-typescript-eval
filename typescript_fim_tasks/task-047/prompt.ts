/* Docstring:
 * Implement `fetchWithFallback` to attempt fetching a resource from multiple URLs until one succeeds.
 * Accept an array of URLs and a fetch-like function returning a promise of a response with an `ok` boolean.
 * Resolve with the first successful response or reject with the last error when all attempts fail.
 */
<｜fim▁begin｜>
export interface FetchLikeResponse {
  ok: boolean;
}

export async function fetchWithFallback(
  urls: string[],
  fetcher: (url: string) => Promise<FetchLikeResponse>,
): Promise<FetchLikeResponse> {
<｜fim▁hole｜>
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
<｜fim▁end｜>
}
