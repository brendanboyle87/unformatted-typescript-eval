/* Docstring:
 * Implement a function `reverseString` that takes a string and returns a new string with the characters in reverse order.
 * The function should handle Unicode characters correctly and must not modify the original string.
 */
<｜fim▁begin｜>
export function reverseString(input: string): string {
  const characters = Array.from(input);
<｜fim▁hole｜>
  for (let left = 0, right = characters.length - 1; left < right; left += 1, right -= 1) {
    const temp = characters[left];
    characters[left] = characters[right];
    characters[right] = temp;
  }
  return characters.join("");
<｜fim▁end｜>
}
