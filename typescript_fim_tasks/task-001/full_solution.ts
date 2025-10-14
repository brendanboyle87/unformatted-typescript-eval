export function reverseString(input: string): string {
  const characters = Array.from(input);
  for (let left = 0, right = characters.length - 1; left < right; left += 1, right -= 1) {
    const temp = characters[left];
    characters[left] = characters[right];
    characters[right] = temp;
  }
  return characters.join("");
}
