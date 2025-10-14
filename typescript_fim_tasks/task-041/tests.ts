import { retryAsync } from './full_solution';

test('retries until success', async () => {
  let attempts = 0;
  const result = await retryAsync(async () => {
    attempts += 1;
    if (attempts < 3) {
      throw new Error('fail');
    }
    return 'ok';
  }, 5);
  expect(result).toBe('ok');
  expect(attempts).toBe(3);
});

test('throws after exhausting attempts', async () => {
  await expect(
    retryAsync(
      async () => {
        throw new Error('always fails');
      },
      2,
    ),
  ).rejects.toThrow('always fails');
});

test('handles zero delay gracefully', async () => {
  let count = 0;
  await expect(
    retryAsync(
      async () => {
        count += 1;
        throw new Error('nope');
      },
      1,
    ),
  ).rejects.toThrow('nope');
  expect(count).toBe(1);
});
