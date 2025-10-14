import { makeCancelable } from './full_solution';

const delay = (ms: number): Promise<void> => new Promise((resolve) => setTimeout(resolve, ms));

test('resolves normally when not cancelled', async () => {
  const { promise, cancel } = makeCancelable(async () => {
    await delay(5);
    return 'done';
  });
  const result = await promise;
  expect(result).toBe('done');
  cancel();
});

test('rejects when cancelled', async () => {
  const { promise, cancel } = makeCancelable(async (signal) => {
    while (!signal.aborted) {
      await delay(5);
    }
    return 'never';
  });
  const rejection = promise.catch((error) => error.message);
  cancel();
  expect(await rejection).toBe('Operation cancelled');
});

test('ignores cancel after resolution', async () => {
  const { promise, cancel } = makeCancelable(async () => 'instant');
  await expect(promise).resolves.toBe('instant');
  expect(() => cancel()).not.toThrow();
});
