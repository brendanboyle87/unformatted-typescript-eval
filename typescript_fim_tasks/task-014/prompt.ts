/* Docstring:
 * Create a function `groupByParity` that partitions an array of integers into even and odd numbers.
 * Return an object with `even` and `odd` properties, each containing the numbers in their original order.
 * The input array should remain unchanged.
 */
<｜fim▁begin｜>
export interface ParityGroups {
  even: number[];
  odd: number[];
}

export function groupByParity(values: number[]): ParityGroups {
<｜fim▁hole｜>
  const even: number[] = [];
  const odd: number[] = [];

  for (const value of values) {
    if (value % 2 === 0) {
      even.push(value);
    } else {
      odd.push(value);
    }
  }

  return { even, odd };
<｜fim▁end｜>
}
