export interface ParityGroups {
  even: number[];
  odd: number[];
}

export function groupByParity(values: number[]): ParityGroups {
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
}
