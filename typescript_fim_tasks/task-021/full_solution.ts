export function bubbleSortNumbers(values: number[]): number[] {
  const result = [...values];
  for (let end = result.length - 1; end > 0; end -= 1) {
    let swapped = false;
    for (let i = 0; i < end; i += 1) {
      if (result[i] > result[i + 1]) {
        [result[i], result[i + 1]] = [result[i + 1], result[i]];
        swapped = true;
      }
    }
    if (!swapped) {
      break;
    }
  }
  return result;
}
