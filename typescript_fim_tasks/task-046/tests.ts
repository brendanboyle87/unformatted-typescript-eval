import { runSequentially } from './full_solution';

test('runs tasks sequentially', async () => {
  const order: number[] = [];
  const results = await runSequentially([
    async () => {
      order.push(1);
      return 'a';
    },
    async () => {
      order.push(2);
      return 'b';
    },
  ]);
  expect(results).toEqual(['a', 'b']);
  expect(order).toEqual([1, 2]);
});

test('handles empty array', async () => {
  expect(await runSequentially([])).toEqual([]);
});

test('propagates errors', async () => {
  await expect(
    runSequentially([
      async () => 'ok',
      async () => {
        throw new Error('fail');
      },
    ]),
  ).rejects.toThrow('fail');
});
