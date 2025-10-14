import { withTimeout } from './full_solution';

test('resolves before timeout', async () => {
  const result = await withTimeout(Promise.resolve('done'), 50);
  expect(result).toBe('done');
});

test('rejects after timeout', async () => {
  await expect(
    withTimeout(
      new Promise<void>((resolve) => setTimeout(resolve, 30)),
      10,
    ),
  ).rejects.toThrow('Operation timed out');
});

test('uses custom message', async () => {
  await expect(withTimeout(new Promise<void>(() => {}), 5, 'Too slow')).rejects.toThrow('Too slow');
});
