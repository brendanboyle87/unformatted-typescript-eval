const normalize = (value: string): string =>
  Array.from(value.toLowerCase())
    .filter((char) => /[\p{Letter}\p{Number}]/u.test(char))
    .sort()
    .join("");

export function areAnagrams(first: string, second: string): boolean {
  const normalizedFirst = normalize(first);
  const normalizedSecond = normalize(second);

  if (normalizedFirst.length !== normalizedSecond.length) {
    return false;
  }

  for (let index = 0; index < normalizedFirst.length; index += 1) {
    if (normalizedFirst[index] !== normalizedSecond[index]) {
      return false;
    }
  }

  return true;
}
