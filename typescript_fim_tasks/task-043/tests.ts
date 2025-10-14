import { pollUntil } from './full_solution';

test('resolves when predicate eventually matches', async () => {
  let count = 0;
  const result = await pollUntil(
    async () => {
      count += 1;
      return count;
    },
    (value) => value >= 3,
    0,
    50,
  );
  expect(result).toBe(3);
});

test('rejects on timeout', async () => {
  await expect(
    pollUntil(
      async () => 0,
      (value) => value === 1,
      5,
      20,
    ),
  ).rejects.toThrow('Polling timed out');
});

test('waits between attempts when interval provided', async () => {
  const start = Date.now();
  let count = 0;
  await pollUntil(
    async () => {
      count += 1;
      return count;
    },
    (value) => value >= 2,
    10,
    100,
  );
  expect(Date.now() - start).toBeGreaterThanOrEqual(10);
});
