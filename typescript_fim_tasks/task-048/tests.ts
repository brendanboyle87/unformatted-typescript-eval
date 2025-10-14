import { memoizeAsync } from './full_solution';

test('caches results for identical arguments', async () => {
  let count = 0;
  const fn = memoizeAsync(async (value: number) => {
    count += 1;
    return value * 2;
  });

  const [first, second] = await Promise.all([fn(2), fn(2)]);
  expect(first).toBe(4);
  expect(second).toBe(4);
  expect(count).toBe(1);
});

test('retries after rejection', async () => {
  let succeed = false;
  const fn = memoizeAsync(async () => {
    if (!succeed) {
      succeed = true;
      throw new Error('fail');
    }
    return 'ok';
  });

  await expect(fn()).rejects.toThrow('fail');
  await expect(fn()).resolves.toBe('ok');
});

test('separates different arguments', async () => {
  const fn = memoizeAsync(async (value: number) => value);
  const results = await Promise.all([fn(1), fn(2)]);
  expect(results).toEqual([1, 2]);
});
