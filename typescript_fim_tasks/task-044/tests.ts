import { limitConcurrency } from './full_solution';

const wait = (ms: number): Promise<void> => new Promise((resolve) => setTimeout(resolve, ms));

test('respects concurrency limit and preserves order', async () => {
  const started: number[] = [];
  const tasks = [
    async () => {
      started.push(1);
      await wait(20);
      return 'a';
    },
    async () => {
      started.push(2);
      await wait(10);
      return 'b';
    },
    async () => {
      started.push(3);
      return 'c';
    },
  ];

  const results = await limitConcurrency(tasks, 2);
  expect(results).toEqual(['a', 'b', 'c']);
  expect(started.slice(0, 2).sort()).toEqual([1, 2]);
});

test('throws on zero limit', async () => {
  await expect(limitConcurrency([], 0)).rejects.toThrow('limit must be greater than 0');
});

test('handles empty task list', async () => {
  const results = await limitConcurrency([], 2);
  expect(results).toEqual([]);
});
