import { fetchWithFallback } from './full_solution';

test('returns first successful response', async () => {
  const calls: string[] = [];
  const response = await fetchWithFallback(
    ['a', 'b'],
    async (url) => {
      calls.push(url);
      if (url === 'b') {
        return { ok: true };
      }
      return { ok: false };
    },
  );
  expect(response.ok).toBe(true);
  expect(calls).toEqual(['a', 'b']);
});

test('rejects when all attempts fail', async () => {
  await expect(
    fetchWithFallback(
      ['a'],
      async () => {
        throw new Error('network');
      },
    ),
  ).rejects.toThrow('network');
});

test('throws when no urls provided', async () => {
  await expect(fetchWithFallback([], async () => ({ ok: true }))).rejects.toThrow('No URLs provided');
});
