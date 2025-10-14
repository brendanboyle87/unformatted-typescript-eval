export function interpolationSearch(values: number[], target: number): number {
  let low = 0;
  let high = values.length - 1;

  while (low <= high && target >= values[low] && target <= values[high]) {
    if (values[low] === values[high]) {
      return values[low] === target ? low : -1;
    }

    const position = low + Math.floor(((target - values[low]) * (high - low)) / (values[high] - values[low]));
    const value = values[position];

    if (value === target) {
      return position;
    }

    if (value < target) {
      low = position + 1;
    } else {
      high = position - 1;
    }
  }

  return -1;
}
