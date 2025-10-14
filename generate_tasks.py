import json
from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent
from typing import List


@dataclass
class Task:
    id: str
    category: str
    function_name: str
    docstring: str
    readme: str
    solution: str
    tests: str


TASKS: List[Task] = []


def add_task(*, id: str, category: str, function_name: str, docstring: str, readme: str, solution: str, tests: str) -> None:
    TASKS.append(
        Task(
            id=id,
            category=category,
            function_name=function_name,
            docstring=docstring.strip(),
            readme=readme.strip(),
            solution=solution.strip(),
            tests=tests.strip(),
        )
    )


add_task(
    id="task-001",
    category="string",
    function_name="reverseString",
    docstring=dedent(
        """
        Implement a function `reverseString` that takes a string and returns a new string with the characters in reverse order.
        The function should handle Unicode characters correctly and must not modify the original string.
        """
    ),
    readme=dedent(
        """
        # Description

        - **Domain:** string
        - Implement `reverseString(input: string): string` to return the characters of `input` in reverse order.
        - Ensure Unicode surrogate pairs remain intact and the original string is not mutated.
        """
    ),
    solution=dedent(
        """
        export function reverseString(input: string): string {
          const characters = Array.from(input);
          // __FIM_HOLE_START__
          for (let left = 0, right = characters.length - 1; left < right; left += 1, right -= 1) {
            const temp = characters[left];
            characters[left] = characters[right];
            characters[right] = temp;
          }
          return characters.join("");
          // __FIM_HOLE_END__
        }
        """
    ),
    tests=dedent(
        """
        import { reverseString } from './full_solution';

        test('reverses ascii word', () => {
          expect(reverseString('hello')).toBe('olleh');
        });

        test('handles empty string', () => {
          expect(reverseString('')).toBe('');
        });

        test('reverses unicode characters', () => {
          expect(reverseString('🙂🙃')).toBe('🙃🙂');
        });
        """
    ),
)


# Additional tasks will be added here.


def main() -> None:
    root = Path('typescript_fim_tasks')
    root.mkdir(exist_ok=True)

    for task in TASKS:
        task_dir = root / task.id
        task_dir.mkdir(parents=True, exist_ok=True)

        readme_path = task_dir / 'README.md'
        readme_path.write_text(task.readme + '\n', encoding='utf-8')

        solution_lines = task.solution.splitlines()

        filtered_solution_lines = [line for line in solution_lines if '// __FIM_HOLE_' not in line]
        solution_path = task_dir / 'full_solution.ts'
        solution_path.write_text('\n'.join(filtered_solution_lines) + '\n', encoding='utf-8')

        try:
            start_idx = next(i for i, line in enumerate(solution_lines) if '// __FIM_HOLE_START__' in line)
            end_idx = next(i for i, line in enumerate(solution_lines) if '// __FIM_HOLE_END__' in line)
        except StopIteration as exc:
            raise ValueError(f"Missing FIM markers in task {task.id}") from exc

        prefix = '\n'.join(solution_lines[:start_idx])
        hole = '\n'.join(line for line in solution_lines[start_idx + 1:end_idx])
        suffix = '\n'.join(solution_lines[end_idx + 1:])

        prompt_content = [
            "/* Docstring:",
            f" * {task.docstring.replace('\n', '\n * ')}",
            " */",
            "<｜fim▁begin｜>",
            prefix,
            "<｜fim▁hole｜>",
            hole,
            "<｜fim▁end｜>",
            suffix,
        ]
        prompt_path = task_dir / 'prompt.ts'
        prompt_path.write_text('\n'.join(prompt_content).strip() + '\n', encoding='utf-8')

        tests_path = task_dir / 'tests.ts'
        tests_path.write_text(task.tests + '\n', encoding='utf-8')

        metadata = {
            "id": task.id,
            "category": task.category,
            "docstring": task.docstring,
            "function": task.function_name,
            "masked_lines": [start_idx + 1, end_idx],
            "num_tests": task.tests.count('test('),
        }
        metadata_path = task_dir / 'metadata.json'
        metadata_path.write_text(json.dumps(metadata, indent=2) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
add_task(
    id="task-002",
    category="string",
    function_name="areAnagrams",
    docstring=dedent(
        """
        Create a function `areAnagrams` that determines whether two input strings are anagrams of each other.
        The function must ignore letter casing and non-alphanumeric characters while performing the comparison.
        Return `true` only if both strings contain the same characters with the same multiplicity once normalized.
        """
    ),
    readme=dedent(
        """
        # Description

        - **Domain:** string
        - Write `areAnagrams(first: string, second: string): boolean` to check if two strings are anagrams once lowercased and stripped of non-alphanumeric characters.
        - Comparison should be Unicode-aware and treat repeated characters with their multiplicity.
        """
    ),
    solution=dedent(
        """
        const normalize = (value: string): string =>
          Array.from(value.toLowerCase())
            .filter((char) => /[\p{Letter}\p{Number}]/u.test(char))
            .sort()
            .join("");

        export function areAnagrams(first: string, second: string): boolean {
          // __FIM_HOLE_START__
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
          // __FIM_HOLE_END__
        }
        """
    ),
    tests=dedent(
        """
        import { areAnagrams } from './full_solution';

        test('detects anagrams with punctuation ignored', () => {
          expect(areAnagrams('Conversation', 'Voices rant on!')).toBe(true);
        });

        test('detects non-anagrams when counts differ', () => {
          expect(areAnagrams('hello', 'heloo')).toBe(false);
        });

        test('handles numeric characters', () => {
          expect(areAnagrams('123', '321')).toBe(true);
        });
        """
    ),
)
add_task(
    id="task-003",
    category="string",
    function_name="capitalizeWords",
    docstring=dedent(
        """
        Build a function `capitalizeWords` that converts the first character of every word in a string to uppercase while lowercasing the remaining characters of the word.
        Words are delimited by whitespace but the original spacing must be preserved in the returned string.
        The function should handle Unicode characters when changing case.
        """
    ),
    readme=dedent(
        """
        # Description

        - **Domain:** string
        - Implement `capitalizeWords(text: string): string` to title-case each whitespace-delimited word while preserving the exact spacing.
        - Use locale-aware casing so Unicode characters are handled correctly.
        """
    ),
    solution=dedent(
        """
        export function capitalizeWords(text: string): string {
          // __FIM_HOLE_START__
          return text
            .split(/(\s+)/)
            .map((segment) => {
              if (/^\s+$/.test(segment) || segment.length === 0) {
                return segment;
              }

              const [first, ...rest] = Array.from(segment);
              const head = first.toLocaleUpperCase();
              const tail = rest.join('').toLocaleLowerCase();
              return `${head}${tail}`;
            })
            .join('');
          // __FIM_HOLE_END__
        }
        """
    ),
    tests=dedent(
        """
        import { capitalizeWords } from './full_solution';

        test('capitalizes words while preserving spaces', () => {
          expect(capitalizeWords('hello   world')).toBe('Hello   World');
        });

        test('handles mixed casing', () => {
          expect(capitalizeWords('gOOD MORNING')).toBe('Good Morning');
        });

        test('supports unicode letters', () => {
          expect(capitalizeWords('über cool')).toBe('Über Cool');
        });
        """
    ),
)
add_task(
    id="task-004",
    category="string",
    function_name="formatCurrency",
    docstring=dedent(
        """
        Implement `formatCurrency` to format a numeric amount as a localized currency string.
        The function accepts the amount, an ISO 4217 currency code, and an optional BCP 47 locale tag defaulting to `en-US`.
        Use `Intl.NumberFormat` and ensure values less than one display at least four decimal places.
        """
    ),
    readme=dedent(
        """
        # Description

        - **Domain:** string
        - Create `formatCurrency(amount: number, currency: string, locale?: string): string` using `Intl.NumberFormat` to produce a localized currency string.
        - Default the locale to `en-US` and show at least four fraction digits when the absolute amount is less than one.
        """
    ),
    solution=dedent(
        """
        export function formatCurrency(amount: number, currency: string, locale = 'en-US'): string {
          // __FIM_HOLE_START__
          const fractionDigits = Math.abs(amount) < 1 ? 4 : 2;
          const formatter = new Intl.NumberFormat(locale, {
            style: 'currency',
            currency,
            minimumFractionDigits: fractionDigits,
            maximumFractionDigits: 4,
          });
          return formatter.format(amount);
          // __FIM_HOLE_END__
        }
        """
    ),
    tests=dedent(
        """
        import { formatCurrency } from './full_solution';

        test('formats usd by default locale', () => {
          expect(formatCurrency(1234.56, 'USD')).toBe('$1,234.56');
        });

        test('shows four decimals for small values', () => {
          expect(formatCurrency(0.1234, 'EUR', 'de-DE')).toBe('0,1234\u00a0€');
        });

        test('handles negative amounts', () => {
          expect(formatCurrency(-42, 'GBP')).toBe('-£42.00');
        });
        """
    ),
)
add_task(
    id="task-005",
    category="string",
    function_name="countVowels",
    docstring=dedent(
        """
        Write a function `countVowels` that counts the number of vowel characters in a string.
        The function accepts a boolean flag `includeY` that, when true, counts the letter `y` as a vowel.
        Return the total number of matching characters while treating the input case-insensitively.
        """
    ),
    readme=dedent(
        """
        # Description

        - **Domain:** string
        - Build `countVowels(text: string, includeY?: boolean): number` to count vowels in `text` in a case-insensitive manner.
        - Include the character `y` when `includeY` is `true` and default the flag to `false`.
        """
    ),
    solution=dedent(
        """
        const BASE_VOWELS = new Set(['a', 'e', 'i', 'o', 'u']);

        export function countVowels(text: string, includeY = false): number {
          // __FIM_HOLE_START__
          let total = 0;
          for (const char of text.toLowerCase()) {
            if (BASE_VOWELS.has(char) || (includeY && char === 'y')) {
              total += 1;
            }
          }
          return total;
          // __FIM_HOLE_END__
        }
        """
    ),
    tests=dedent(
        """
        import { countVowels } from './full_solution';

        test('counts vowels in lowercase', () => {
          expect(countVowels('hello world')).toBe(3);
        });

        test('is case insensitive', () => {
          expect(countVowels('AEIOU')).toBe(5);
        });

        test('optionally counts y', () => {
          expect(countVowels('rhythms', true)).toBe(1);
        });
        """
    ),
)
add_task(
    id="task-006",
    category="string",
    function_name="snakeToCamel",
    docstring=dedent(
        """
        Implement `snakeToCamel` to convert a snake_case string to camelCase.
        The function should lowercase the first segment and capitalize the first letter of subsequent segments while removing underscores.
        Empty segments caused by consecutive underscores should be skipped in the output.
        """
    ),
    readme=dedent(
        """
        # Description

        - **Domain:** string
        - Create `snakeToCamel(value: string): string` that transforms snake_case identifiers into camelCase.
        - Collapse duplicate underscores and ignore empty segments when building the final string.
        """
    ),
    solution=dedent(
        """
        export function snakeToCamel(value: string): string {
          // __FIM_HOLE_START__
          const segments = value.split('_');
          return segments
            .filter((segment) => segment.length > 0)
            .map((segment, index) => {
              const lower = segment.toLowerCase();
              if (index === 0) {
                return lower;
              }
              const [first, ...rest] = lower;
              return `${first.toUpperCase()}${rest.join('')}`;
            })
            .join('');
          // __FIM_HOLE_END__
        }
        """
    ),
    tests=dedent(
        """
        import { snakeToCamel } from './full_solution';

        test('converts simple snake to camel', () => {
          expect(snakeToCamel('hello_world')).toBe('helloWorld');
        });

        test('handles consecutive underscores', () => {
          expect(snakeToCamel('__make__everything__work__')).toBe('makeEverythingWork');
        });

        test('preserves lowercase first segment', () => {
          expect(snakeToCamel('Already_Lower')).toBe('alreadyLower');
        });
        """
    ),
)
add_task(
    id="task-007",
    category="string",
    function_name="truncateString",
    docstring=dedent(
        """
        Create `truncateString` to shorten a string to a maximum length, appending an ellipsis by default when truncation occurs.
        Accept the original text, the maximum allowed length, and an optional ellipsis string defaulting to `…`.
        Throw a `RangeError` if the maximum length is negative, and ensure the returned string does not exceed the limit.
        """
    ),
    readme=dedent(
        """
        # Description

        - **Domain:** string
        - Implement `truncateString(text: string, maxLength: number, ellipsis?: string): string` to constrain the length of `text`.
        - Use `…` as the default suffix, trimming it if the limit is shorter than the ellipsis itself.
        """
    ),
    solution=dedent(
        """
        export function truncateString(text: string, maxLength: number, ellipsis = '…'): string {
          // __FIM_HOLE_START__
          if (maxLength < 0) {
            throw new RangeError('maxLength must be non-negative');
          }

          if (text.length <= maxLength) {
            return text;
          }

          if (maxLength <= ellipsis.length) {
            return ellipsis.slice(0, maxLength);
          }

          const sliceEnd = maxLength - ellipsis.length;
          return `${text.slice(0, sliceEnd)}${ellipsis}`;
          // __FIM_HOLE_END__
        }
        """
    ),
    tests=dedent(
        """
        import { truncateString } from './full_solution';

        test('returns original when below limit', () => {
          expect(truncateString('hello', 10)).toBe('hello');
        });

        test('applies ellipsis when truncated', () => {
          expect(truncateString('typescript', 6)).toBe('type…');
        });

        test('throws on negative length', () => {
          expect(() => truncateString('test', -1)).toThrow(RangeError);
        });
        """
    ),
)
add_task(
    id="task-008",
    category="string",
    function_name="padCenter",
    docstring=dedent(
        """
        Design `padCenter` to center a string within a target length by padding with a specified character.
        The function receives the text, the desired total length, and an optional single-character pad value defaulting to a space.
        Throw an error when the pad value is not exactly one character long and return the original text if no padding is needed.
        """
    ),
    readme=dedent(
        """
        # Description

        - **Domain:** string
        - Implement `padCenter(text: string, targetLength: number, padChar?: string): string` to center-align `text` by padding both sides.
        - Use space as the default pad character, rounding extra padding to the right when the difference is odd.
        """
    ),
    solution=dedent(
        """
        export function padCenter(text: string, targetLength: number, padChar = ' '): string {
          // __FIM_HOLE_START__
          if (padChar.length !== 1) {
            throw new Error('padChar must be exactly one character');
          }

          if (text.length >= targetLength) {
            return text;
          }

          const padding = targetLength - text.length;
          const left = Math.floor(padding / 2);
          const right = padding - left;
          return `${padChar.repeat(left)}${text}${padChar.repeat(right)}`;
          // __FIM_HOLE_END__
        }
        """
    ),
    tests=dedent(
        """
        import { padCenter } from './full_solution';

        test('centers string with spaces', () => {
          expect(padCenter('cat', 7)).toBe('  cat  ');
        });

        test('prefers extra padding on the right', () => {
          expect(padCenter('go', 5, '.')).toBe('.go..');
        });

        test('throws when padChar is invalid', () => {
          expect(() => padCenter('test', 6, 'xx')).toThrow('padChar must be exactly one character');
        });
        """
    ),
)
add_task(
    id="task-009",
    category="string",
    function_name="repeatPattern",
    docstring=dedent(
        """
        Implement `repeatPattern` to produce a string of a specified length by repeating a pattern.
        The function takes a pattern string and the desired total length; it should truncate the last repetition to fit the limit.
        Throw a `RangeError` when the requested length is negative and return an empty string if the pattern is empty.
        """
    ),
    readme=dedent(
        """
        # Description

        - **Domain:** string
        - Write `repeatPattern(pattern: string, length: number): string` that repeats `pattern` until `length` characters are produced.
        - Trim the final repetition to avoid exceeding the requested length and guard against negative inputs.
        """
    ),
    solution=dedent(
        """
        export function repeatPattern(pattern: string, length: number): string {
          // __FIM_HOLE_START__
          if (length < 0) {
            throw new RangeError('length must be non-negative');
          }

          if (pattern.length === 0 || length === 0) {
            return '';
          }

          let result = '';
          while (result.length < length) {
            const remaining = length - result.length;
            result += remaining >= pattern.length ? pattern : pattern.slice(0, remaining);
          }

          return result;
          // __FIM_HOLE_END__
        }
        """
    ),
    tests=dedent(
        """
        import { repeatPattern } from './full_solution';

        test('repeats pattern to desired length', () => {
          expect(repeatPattern('ab', 5)).toBe('ababa');
        });

        test('handles empty pattern', () => {
          expect(repeatPattern('', 5)).toBe('');
        });

        test('throws for negative length', () => {
          expect(() => repeatPattern('ab', -1)).toThrow(RangeError);
        });
        """
    ),
)
add_task(
    id="task-010",
    category="string",
    function_name="highlightKeyword",
    docstring=dedent(
        """
        Implement `highlightKeyword` to wrap all case-insensitive occurrences of a keyword within a text string.
        The function receives the text, the keyword, and an optional wrapper object containing `start` and `end` strings defaulting to `<mark>` and `</mark>`.
        Escape special regex characters in the keyword and leave the text unchanged when the keyword is empty.
        """
    ),
    readme=dedent(
        """
        # Description

        - **Domain:** string
        - Write `highlightKeyword(text: string, keyword: string, wrapper?: { start: string; end: string }): string` to highlight keyword occurrences.
        - Perform a case-insensitive search, escaping any regex metacharacters in the keyword before replacement.
        """
    ),
    solution=dedent(
        """
        export interface HighlightWrapper {
          start: string;
          end: string;
        }

        const escapeRegex = (value: string): string => value.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');

        export function highlightKeyword(
          text: string,
          keyword: string,
          wrapper: HighlightWrapper = { start: '<mark>', end: '</mark>' },
        ): string {
          // __FIM_HOLE_START__
          if (keyword.length === 0) {
            return text;
          }

          const escaped = escapeRegex(keyword);
          const pattern = new RegExp(escaped, 'gi');
          return text.replace(pattern, (match) => `${wrapper.start}${match}${wrapper.end}`);
          // __FIM_HOLE_END__
        }
        """
    ),
    tests=dedent(
        """
        import { highlightKeyword } from './full_solution';

        test('wraps occurrences with default markup', () => {
          expect(highlightKeyword('Learn TypeScript with TypeScript', 'typescript')).toBe('Learn <mark>TypeScript</mark> with <mark>TypeScript</mark>');
        });

        test('uses custom wrapper', () => {
          expect(highlightKeyword('1 + 1 = 2', '+', { start: '[', end: ']' })).toBe('1 [+] 1 = 2');
        });

        test('leaves text unchanged for empty keyword', () => {
          expect(highlightKeyword('sample', '')).toBe('sample');
        });
        """
    ),
)
add_task(
    id="task-011",
    category="array",
    function_name="uniqueNumbers",
    docstring=dedent(
        """
        Implement `uniqueNumbers` to return an array containing only the first occurrence of each number in the input sequence.
        Preserve the original order of the numbers and do not mutate the provided array.
        The function should handle negative numbers and `NaN` values correctly.
        """
    ),
    readme=dedent(
        """
        # Description

        - **Domain:** array
        - Create `uniqueNumbers(values: number[]): number[]` that removes duplicates while preserving order.
        - Treat `NaN` as a single distinct value and avoid altering the original array.
        """
    ),
    solution=dedent(
        """
        export function uniqueNumbers(values: number[]): number[] {
          // __FIM_HOLE_START__
          const seen = new Set<number>();
          let seenNaN = false;
          const result: number[] = [];

          for (const value of values) {
            if (Number.isNaN(value)) {
              if (!seenNaN) {
                seenNaN = true;
                result.push(value);
              }
              continue;
            }

            if (!seen.has(value)) {
              seen.add(value);
              result.push(value);
            }
          }

          return result;
          // __FIM_HOLE_END__
        }
        """
    ),
    tests=dedent(
        """
        import { uniqueNumbers } from './full_solution';

        test('removes duplicates preserving order', () => {
          expect(uniqueNumbers([1, 2, 1, 3, 2])).toEqual([1, 2, 3]);
        });

        test('handles negative numbers', () => {
          expect(uniqueNumbers([-1, -1, -2])).toEqual([-1, -2]);
        });

        test('treats NaN as a single unique value', () => {
          const result = uniqueNumbers([NaN, NaN, 1]);
          expect(result.length).toBe(2);
          expect(Number.isNaN(result[0])).toBe(true);
          expect(result[1]).toBe(1);
        });
        """
    ),
)
add_task(
    id="task-012",
    category="array",
    function_name="flattenOneLevel",
    docstring=dedent(
        """
        Write a generic function `flattenOneLevel` that flattens an array by one depth.
        The input array may contain elements of type `T` or arrays of `T`, and the output should be a new array of `T`.
        The original array must not be mutated.
        """
    ),
    readme=dedent(
        """
        # Description

        - **Domain:** array
        - Implement `flattenOneLevel<T>(input: (T | T[])[]): T[]` to merge nested arrays one level deep.
        - Preserve the order of elements and avoid mutating the input array.
        """
    ),
    solution=dedent(
        """
        export function flattenOneLevel<T>(input: (T | T[])[]): T[] {
          // __FIM_HOLE_START__
          const result: T[] = [];
          for (const element of input) {
            if (Array.isArray(element)) {
              result.push(...element);
            } else {
              result.push(element);
            }
          }
          return result;
          // __FIM_HOLE_END__
        }
        """
    ),
    tests=dedent(
        """
        import { flattenOneLevel } from './full_solution';

        test('flattens arrays one level deep', () => {
          expect(flattenOneLevel([1, [2, 3], 4])).toEqual([1, 2, 3, 4]);
        });

        test('preserves nested arrays beyond one level', () => {
          expect(flattenOneLevel([1, [2, [3]], 4])).toEqual([1, 2, [3], 4]);
        });

        test('handles empty array', () => {
          expect(flattenOneLevel<number>([])).toEqual([]);
        });
        """
    ),
)
add_task(
    id="task-013",
    category="array",
    function_name="chunkArray",
    docstring=dedent(
        """
        Implement `chunkArray` that splits an array into equally sized chunks except possibly the last chunk.
        Accept the input array and a positive chunk size; throw an error if the size is less than one.
        Return a new array of chunk arrays without mutating the original input.
        """
    ),
    readme=dedent(
        """
        # Description

        - **Domain:** array
        - Write `chunkArray<T>(items: T[], size: number): T[][]` to partition `items` into arrays of length `size`.
        - Preserve the order and throw an error when `size` is zero or negative.
        """
    ),
    solution=dedent(
        """
        export function chunkArray<T>(items: T[], size: number): T[][] {
          // __FIM_HOLE_START__
          if (size <= 0) {
            throw new Error('size must be greater than zero');
          }

          const result: T[][] = [];
          for (let index = 0; index < items.length; index += size) {
            result.push(items.slice(index, index + size));
          }

          return result;
          // __FIM_HOLE_END__
        }
        """
    ),
    tests=dedent(
        """
        import { chunkArray } from './full_solution';

        test('chunks array into equal parts', () => {
          expect(chunkArray([1, 2, 3, 4], 2)).toEqual([[1, 2], [3, 4]]);
        });

        test('handles remainder chunk', () => {
          expect(chunkArray([1, 2, 3, 4, 5], 2)).toEqual([[1, 2], [3, 4], [5]]);
        });

        test('throws on invalid size', () => {
          expect(() => chunkArray([1, 2, 3], 0)).toThrow('size must be greater than zero');
        });
        """
    ),
)
add_task(
    id="task-014",
    category="array",
    function_name="groupByParity",
    docstring=dedent(
        """
        Create a function `groupByParity` that partitions an array of integers into even and odd numbers.
        Return an object with `even` and `odd` properties, each containing the numbers in their original order.
        The input array should remain unchanged.
        """
    ),
    readme=dedent(
        """
        # Description

        - **Domain:** array
        - Implement `groupByParity(values: number[]): { even: number[]; odd: number[] }` to classify integers by parity.
        - Keep the order of numbers as they appear in the input.
        """
    ),
    solution=dedent(
        """
        export interface ParityGroups {
          even: number[];
          odd: number[];
        }

        export function groupByParity(values: number[]): ParityGroups {
          // __FIM_HOLE_START__
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
          // __FIM_HOLE_END__
        }
        """
    ),
    tests=dedent(
        """
        import { groupByParity } from './full_solution';

        test('splits numbers by parity', () => {
          expect(groupByParity([1, 2, 3, 4])).toEqual({ even: [2, 4], odd: [1, 3] });
        });

        test('handles empty input', () => {
          expect(groupByParity([])).toEqual({ even: [], odd: [] });
        });

        test('preserves order', () => {
          expect(groupByParity([3, 2, 2, 5]).even).toEqual([2, 2]);
        });
        """
    ),
)
add_task(
    id="task-015",
    category="array",
    function_name="getTopNElements",
    docstring=dedent(
        """
        Implement `getTopNElements` to return the largest `n` numbers from an array sorted in descending order.
        The original array must remain unchanged and `n` should be clamped between zero and the array length.
        Handle duplicate numbers by including them according to their frequency.
        """
    ),
    readme=dedent(
        """
        # Description

        - **Domain:** array
        - Create `getTopNElements(values: number[], n: number): number[]` to extract the `n` largest numbers in descending order.
        - Clamp `n` to `[0, values.length]` and avoid mutating the input array.
        """
    ),
    solution=dedent(
        """
        export function getTopNElements(values: number[], n: number): number[] {
          // __FIM_HOLE_START__
          if (n <= 0) {
            return [];
          }

          const count = Math.min(n, values.length);
          const copy = [...values];
          copy.sort((a, b) => b - a);
          return copy.slice(0, count);
          // __FIM_HOLE_END__
        }
        """
    ),
    tests=dedent(
        """
        import { getTopNElements } from './full_solution';

        test('returns top elements', () => {
          expect(getTopNElements([5, 1, 3, 4], 2)).toEqual([5, 4]);
        });

        test('handles n larger than array length', () => {
          expect(getTopNElements([1, 2], 5)).toEqual([2, 1]);
        });

        test('returns empty when n <= 0', () => {
          expect(getTopNElements([1, 2, 3], 0)).toEqual([]);
        });
        """
    ),
)
add_task(
    id="task-016",
    category="array",
    function_name="findMissingNumbers",
    docstring=dedent(
        """
        Implement `findMissingNumbers` to identify the integers missing from a sequence.
        Given an array of integers (in any order), return the numbers that do not appear between the minimum and maximum values inclusive.
        Return an empty array when the input is empty or contains a complete range.
        """
    ),
    readme=dedent(
        """
        # Description

        - **Domain:** array
        - Create `findMissingNumbers(values: number[]): number[]` to list integers absent from the inclusive range defined by the minimum and maximum of `values`.
        - Ignore duplicates in the input and return an empty array when the sequence is complete or empty.
        """
    ),
    solution=dedent(
        """
        export function findMissingNumbers(values: number[]): number[] {
          // __FIM_HOLE_START__
          if (values.length === 0) {
            return [];
          }

          const min = Math.min(...values);
          const max = Math.max(...values);
          const set = new Set(values);
          const missing: number[] = [];

          for (let number = min; number <= max; number += 1) {
            if (!set.has(number)) {
              missing.push(number);
            }
          }

          return missing;
          // __FIM_HOLE_END__
        }
        """
    ),
    tests=dedent(
        """
        import { findMissingNumbers } from './full_solution';

        test('finds missing numbers within range', () => {
          expect(findMissingNumbers([1, 4, 2])).toEqual([3]);
        });

        test('returns empty for continuous sequence', () => {
          expect(findMissingNumbers([3, 2, 1])).toEqual([]);
        });

        test('handles empty input', () => {
          expect(findMissingNumbers([])).toEqual([]);
        });
        """
    ),
)
add_task(
    id="task-017",
    category="array",
    function_name="rotateArray",
    docstring=dedent(
        """
        Implement `rotateArray` to rotate an array of elements by a given number of steps to the right.
        The rotation count may be negative, indicating a rotation to the left.
        Return a new array without modifying the original input.
        """
    ),
    readme=dedent(
        """
        # Description

        - **Domain:** array
        - Write `rotateArray<T>(items: T[], steps: number): T[]` that rotates `items` right when `steps` is positive and left when negative.
        - Handle rotation counts larger than the array length using modular arithmetic and do not mutate the input array.
        """
    ),
    solution=dedent(
        """
        export function rotateArray<T>(items: T[], steps: number): T[] {
          // __FIM_HOLE_START__
          if (items.length === 0) {
            return [];
          }

          const normalized = ((steps % items.length) + items.length) % items.length;
          if (normalized === 0) {
            return [...items];
          }

          const splitIndex = items.length - normalized;
          return [...items.slice(splitIndex), ...items.slice(0, splitIndex)];
          // __FIM_HOLE_END__
        }
        """
    ),
    tests=dedent(
        """
        import { rotateArray } from './full_solution';

        test('rotates to the right', () => {
          expect(rotateArray([1, 2, 3, 4], 1)).toEqual([4, 1, 2, 3]);
        });

        test('rotates to the left when negative', () => {
          expect(rotateArray([1, 2, 3, 4], -1)).toEqual([2, 3, 4, 1]);
        });

        test('handles rotation greater than length', () => {
          expect(rotateArray([1, 2, 3], 5)).toEqual([2, 3, 1]);
        });
        """
    ),
)
add_task(
    id="task-018",
    category="array",
    function_name="sumByKey",
    docstring=dedent(
        """
        Implement `sumByKey` to sum numeric property values across an array of objects.
        Accept an array of generic records and a key; treat missing or non-number values as zero.
        Return the total sum as a number.
        """
    ),
    readme=dedent(
        """
        # Description

        - **Domain:** array
        - Write `sumByKey<T extends Record<string, unknown>>(items: T[], key: keyof T): number` to add all numeric values for `key`.
        - Ignore entries where the key is absent or not a finite number.
        """
    ),
    solution=dedent(
        """
        export function sumByKey<T extends Record<string, unknown>>(items: T[], key: keyof T): number {
          // __FIM_HOLE_START__
          let total = 0;
          for (const item of items) {
            const value = item[key];
            if (typeof value === 'number' && Number.isFinite(value)) {
              total += value;
            }
          }
          return total;
          // __FIM_HOLE_END__
        }
        """
    ),
    tests=dedent(
        """
        import { sumByKey } from './full_solution';

        test('sums numeric values', () => {
          expect(sumByKey([{ value: 2 }, { value: 3 }], 'value')).toBe(5);
        });

        test('ignores missing keys', () => {
          expect(sumByKey([{ value: 2 }, {} as { value: number }], 'value')).toBe(2);
        });

        test('skips non-numeric values', () => {
          expect(sumByKey<{ value: unknown }>([{ value: '3' }, { value: 4 }, { value: Number.POSITIVE_INFINITY }], 'value')).toBe(4);
        });
        """
    ),
)
add_task(
    id="task-019",
    category="array",
    function_name="filterTruthy",
    docstring=dedent(
        """
        Create `filterTruthy` to remove falsy values from an array.
        The function should return a new array containing only values that coerce to true, preserving the original order.
        TypeScript should infer the narrowed type of the returned array.
        """
    ),
    readme=dedent(
        """
        # Description

        - **Domain:** array
        - Implement `filterTruthy<T>(values: T[]): Array<NonNullable<T>>` to remove falsy entries such as `0`, `''`, `false`, `null`, and `undefined`.
        - Preserve the order of truthy elements without mutating the input array.
        """
    ),
    solution=dedent(
        """
        export function filterTruthy<T>(values: T[]): Array<NonNullable<T>> {
          // __FIM_HOLE_START__
          return values.filter((value): value is NonNullable<T> => Boolean(value));
          // __FIM_HOLE_END__
        }
        """
    ),
    tests=dedent(
        """
        import { filterTruthy } from './full_solution';

        test('filters out falsy values', () => {
          expect(filterTruthy([0, 1, '', 'hello', null, undefined])).toEqual([1, 'hello']);
        });

        test('preserves true booleans', () => {
          expect(filterTruthy([false, true, true])).toEqual([true, true]);
        });

        test('handles empty array', () => {
          expect(filterTruthy([])).toEqual([]);
        });
        """
    ),
)
add_task(
    id="task-020",
    category="array",
    function_name="mergeSortedArrays",
    docstring=dedent(
        """
        Implement `mergeSortedArrays` to merge two sorted arrays of numbers into a single sorted array.
        Both inputs are sorted in ascending order; the result should also be ascending and include duplicates.
        The original arrays must not be modified.
        """
    ),
    readme=dedent(
        """
        # Description

        - **Domain:** array
        - Write `mergeSortedArrays(left: number[], right: number[]): number[]` to combine two ascending arrays.
        - Preserve duplicate values and avoid mutating either input array.
        """
    ),
    solution=dedent(
        """
        export function mergeSortedArrays(left: number[], right: number[]): number[] {
          // __FIM_HOLE_START__
          const result: number[] = [];
          let i = 0;
          let j = 0;

          while (i < left.length && j < right.length) {
            if (left[i] <= right[j]) {
              result.push(left[i]);
              i += 1;
            } else {
              result.push(right[j]);
              j += 1;
            }
          }

          while (i < left.length) {
            result.push(left[i]);
            i += 1;
          }

          while (j < right.length) {
            result.push(right[j]);
            j += 1;
          }

          return result;
          // __FIM_HOLE_END__
        }
        """
    ),
    tests=dedent(
        """
        import { mergeSortedArrays } from './full_solution';

        test('merges two sorted arrays', () => {
          expect(mergeSortedArrays([1, 3, 5], [2, 4, 6])).toEqual([1, 2, 3, 4, 5, 6]);
        });

        test('includes duplicates', () => {
          expect(mergeSortedArrays([1, 2, 2], [2, 3])).toEqual([1, 2, 2, 2, 3]);
        });

        test('handles empty arrays', () => {
          expect(mergeSortedArrays([], [1, 2])).toEqual([1, 2]);
        });
        """
    ),
)
add_task(
    id="task-021",
    category="sorting_search",
    function_name="bubbleSortNumbers",
    docstring=dedent(
        """
        Implement `bubbleSortNumbers` to sort an array of numbers in ascending order using the bubble sort algorithm.
        Return a new array without mutating the original input.
        Optimize by stopping early when no swaps occur during a pass.
        """
    ),
    readme=dedent(
        """
        # Description

        - **Domain:** sorting/search
        - Create `bubbleSortNumbers(values: number[]): number[]` to sort numbers using bubble sort with an early exit optimization.
        - Return a sorted copy, leaving the input array unchanged.
        """
    ),
    solution=dedent(
        """
        export function bubbleSortNumbers(values: number[]): number[] {
          // __FIM_HOLE_START__
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
          // __FIM_HOLE_END__
        }
        """
    ),
    tests=dedent(
        """
        import { bubbleSortNumbers } from './full_solution';

        test('sorts numbers ascending', () => {
          expect(bubbleSortNumbers([3, 2, 5, 1])).toEqual([1, 2, 3, 5]);
        });

        test('handles already sorted array efficiently', () => {
          expect(bubbleSortNumbers([1, 2, 3])).toEqual([1, 2, 3]);
        });

        test('works with duplicates', () => {
          expect(bubbleSortNumbers([3, 3, 2])).toEqual([2, 3, 3]);
        });
        """
    ),
)
add_task(
    id="task-022",
    category="sorting_search",
    function_name="quickSortStrings",
    docstring=dedent(
        """
        Implement `quickSortStrings` to sort strings in ascending order using the quicksort algorithm.
        Compare strings using `localeCompare` with base sensitivity to perform a case-insensitive sort.
        Return a new sorted array without mutating the input.
        """
    ),
    readme=dedent(
        """
        # Description

        - **Domain:** sorting/search
        - Write `quickSortStrings(values: string[]): string[]` that sorts strings case-insensitively using quicksort.
        - Use `localeCompare` with `{ sensitivity: 'base' }` to compare values and avoid mutating the input array.
        """
    ),
    solution=dedent(
        """
        export function quickSortStrings(values: string[]): string[] {
          // __FIM_HOLE_START__
          if (values.length <= 1) {
            return [...values];
          }

          const [pivot, ...rest] = values;
          const left: string[] = [];
          const right: string[] = [];

          for (const value of rest) {
            const comparison = value.localeCompare(pivot, undefined, { sensitivity: 'base' });
            if (comparison < 0) {
              left.push(value);
            } else if (comparison > 0) {
              right.push(value);
            } else {
              right.push(value);
            }
          }

          return [...quickSortStrings(left), pivot, ...quickSortStrings(right)];
          // __FIM_HOLE_END__
        }
        """
    ),
    tests=dedent(
        """
        import { quickSortStrings } from './full_solution';

        test('sorts strings ignoring case', () => {
          expect(quickSortStrings(['Banana', 'apple', 'cherry'])).toEqual(['apple', 'Banana', 'cherry']);
        });

        test('handles already sorted list', () => {
          expect(quickSortStrings(['a', 'b', 'c'])).toEqual(['a', 'b', 'c']);
        });

        test('handles duplicates', () => {
          expect(quickSortStrings(['a', 'A', 'b'])).toEqual(['a', 'A', 'b']);
        });
        """
    ),
)
add_task(
    id="task-023",
    category="sorting_search",
    function_name="binarySearch",
    docstring=dedent(
        """
        Implement `binarySearch` to locate a target number within a sorted ascending array of numbers.
        Return the index of the target if found or `-1` otherwise.
        Use an iterative binary search algorithm with `O(log n)` complexity.
        """
    ),
    readme=dedent(
        """
        # Description

        - **Domain:** sorting/search
        - Write `binarySearch(values: number[], target: number): number` that searches for `target` in a sorted ascending array.
        - Return the index when found or `-1` if the value is absent using an iterative binary search.
        """
    ),
    solution=dedent(
        """
        export function binarySearch(values: number[], target: number): number {
          // __FIM_HOLE_START__
          let low = 0;
          let high = values.length - 1;

          while (low <= high) {
            const mid = Math.floor((low + high) / 2);
            const value = values[mid];

            if (value === target) {
              return mid;
            }

            if (value < target) {
              low = mid + 1;
            } else {
              high = mid - 1;
            }
          }

          return -1;
          // __FIM_HOLE_END__
        }
        """
    ),
    tests=dedent(
        """
        import { binarySearch } from './full_solution';

        test('finds existing element', () => {
          expect(binarySearch([1, 3, 5, 7], 5)).toBe(2);
        });

        test('returns -1 when not found', () => {
          expect(binarySearch([1, 3, 5, 7], 4)).toBe(-1);
        });

        test('handles empty array', () => {
          expect(binarySearch([], 1)).toBe(-1);
        });
        """
    ),
)
add_task(
    id="task-024",
    category="sorting_search",
    function_name="insertionSortByKey",
    docstring=dedent(
        """
        Implement `insertionSortByKey` to sort an array of objects using the insertion sort algorithm.
        The function accepts an array of records and a key whose numeric values determine the ordering.
        Return a new array sorted ascending by the key without mutating the original.
        """
    ),
    readme=dedent(
        """
        # Description

        - **Domain:** sorting/search
        - Write `insertionSortByKey<T extends Record<string, unknown>>(items: T[], key: keyof T): T[]` to sort objects by a numeric key using insertion sort.
        - Return a sorted copy, leaving the input array unchanged.
        """
    ),
    solution=dedent(
        """
        export function insertionSortByKey<T extends Record<string, unknown>>(items: T[], key: keyof T): T[] {
          // __FIM_HOLE_START__
          const result = items.map((item) => ({ ...item }));

          for (let i = 1; i < result.length; i += 1) {
            const current = result[i];
            let j = i - 1;

            while (j >= 0 && Number(result[j][key]) > Number(current[key])) {
              result[j + 1] = result[j];
              j -= 1;
            }

            result[j + 1] = current;
          }

          return result;
          // __FIM_HOLE_END__
        }
        """
    ),
    tests=dedent(
        """
        import { insertionSortByKey } from './full_solution';

        test('sorts objects by numeric key', () => {
          const sorted = insertionSortByKey(
            [
              { id: 3, name: 'c' },
              { id: 1, name: 'a' },
              { id: 2, name: 'b' },
            ],
            'id',
          );
          expect(sorted.map((item) => item.id)).toEqual([1, 2, 3]);
        });

        test('does not mutate original array', () => {
          const input = [{ score: 2 }, { score: 1 }];
          insertionSortByKey(input, 'score');
          expect(input).toEqual([{ score: 2 }, { score: 1 }]);
        });

        test('handles empty array', () => {
          expect(insertionSortByKey([], 'value')).toEqual([]);
        });
        """
    ),
)
add_task(
    id="task-025",
    category="sorting_search",
    function_name="mergeSort",
    docstring=dedent(
        """
        Implement `mergeSort` to sort an array of numbers in ascending order using the merge sort algorithm.
        The function should recursively divide the array and merge sorted halves, returning a new array.
        Do not mutate the input array.
        """
    ),
    readme=dedent(
        """
        # Description

        - **Domain:** sorting/search
        - Write `mergeSort(values: number[]): number[]` that uses merge sort to sort numbers ascending.
        - Return a sorted copy of the input array.
        """
    ),
    solution=dedent(
        """
        const merge = (left: number[], right: number[]): number[] => {
          const result: number[] = [];
          let i = 0;
          let j = 0;

          while (i < left.length && j < right.length) {
            if (left[i] <= right[j]) {
              result.push(left[i]);
              i += 1;
            } else {
              result.push(right[j]);
              j += 1;
            }
          }

          return result.concat(left.slice(i)).concat(right.slice(j));
        };

        export function mergeSort(values: number[]): number[] {
          // __FIM_HOLE_START__
          if (values.length <= 1) {
            return [...values];
          }

          const middle = Math.floor(values.length / 2);
          const left = mergeSort(values.slice(0, middle));
          const right = mergeSort(values.slice(middle));
          return merge(left, right);
          // __FIM_HOLE_END__
        }
        """
    ),
    tests=dedent(
        """
        import { mergeSort } from './full_solution';

        test('sorts numbers using merge sort', () => {
          expect(mergeSort([5, 2, 4, 6, 1, 3])).toEqual([1, 2, 3, 4, 5, 6]);
        });

        test('returns new array for single element', () => {
          const input = [1];
          const output = mergeSort(input);
          expect(output).toEqual([1]);
          expect(output).not.toBe(input);
        });

        test('handles empty array', () => {
          expect(mergeSort([])).toEqual([]);
        });
        """
    ),
)
add_task(
    id="task-026",
    category="sorting_search",
    function_name="findKthSmallest",
    docstring=dedent(
        """
        Implement `findKthSmallest` to return the k-th smallest number in an unsorted array.
        The function should use a selection algorithm with average `O(n)` time complexity and not mutate the input array.
        Throw a `RangeError` when `k` is out of bounds (less than 1 or greater than the array length).
        """
    ),
    readme=dedent(
        """
        # Description

        - **Domain:** sorting/search
        - Write `findKthSmallest(values: number[], k: number): number` using the quickselect algorithm to locate the k-th smallest value.
        - Validate `k` and operate on a copy of the array to keep the original untouched.
        """
    ),
    solution=dedent(
        """
        const partition = (array: number[], left: number, right: number, pivotIndex: number): number => {
          const pivotValue = array[pivotIndex];
          [array[pivotIndex], array[right]] = [array[right], array[pivotIndex]];
          let storeIndex = left;

          for (let i = left; i < right; i += 1) {
            if (array[i] < pivotValue) {
              [array[i], array[storeIndex]] = [array[storeIndex], array[i]];
              storeIndex += 1;
            }
          }

          [array[right], array[storeIndex]] = [array[storeIndex], array[right]];
          return storeIndex;
        };

        export function findKthSmallest(values: number[], k: number): number {
          // __FIM_HOLE_START__
          if (k < 1 || k > values.length) {
            throw new RangeError('k is out of range');
          }

          const array = [...values];
          let left = 0;
          let right = array.length - 1;
          const target = k - 1;

          while (true) {
            const pivotIndex = partition(array, left, right, Math.floor((left + right) / 2));

            if (pivotIndex === target) {
              return array[pivotIndex];
            }

            if (target < pivotIndex) {
              right = pivotIndex - 1;
            } else {
              left = pivotIndex + 1;
            }
          }
          // __FIM_HOLE_END__
        }
        """
    ),
    tests=dedent(
        """
        import { findKthSmallest } from './full_solution';

        test('finds first smallest', () => {
          expect(findKthSmallest([3, 1, 2], 1)).toBe(1);
        });

        test('finds middle element', () => {
          expect(findKthSmallest([7, 4, 6, 3, 9, 1], 3)).toBe(4);
        });

        test('throws on invalid k', () => {
          expect(() => findKthSmallest([1, 2, 3], 0)).toThrow(RangeError);
        });
        """
    ),
)
add_task(
    id="task-027",
    category="sorting_search",
    function_name="searchMatrix",
    docstring=dedent(
        """
        Implement `searchMatrix` to determine whether a target number exists in a 2D matrix.
        Each row of the matrix is sorted in ascending order and the first element of each row is greater than the last element of the previous row.
        Use binary search across the flattened matrix and return a boolean indicating whether the target is present.
        """
    ),
    readme=dedent(
        """
        # Description

        - **Domain:** sorting/search
        - Write `searchMatrix(matrix: number[][], target: number): boolean` to search the matrix using binary search treating it as a flattened sorted array.
        - Return `true` when the target exists; otherwise `false`.
        """
    ),
    solution=dedent(
        """
        export function searchMatrix(matrix: number[][], target: number): boolean {
          // __FIM_HOLE_START__
          if (matrix.length === 0 || matrix[0].length === 0) {
            return false;
          }

          const rows = matrix.length;
          const cols = matrix[0].length;
          let low = 0;
          let high = rows * cols - 1;

          while (low <= high) {
            const mid = Math.floor((low + high) / 2);
            const row = Math.floor(mid / cols);
            const col = mid % cols;
            const value = matrix[row][col];

            if (value === target) {
              return true;
            }

            if (value < target) {
              low = mid + 1;
            } else {
              high = mid - 1;
            }
          }

          return false;
          // __FIM_HOLE_END__
        }
        """
    ),
    tests=dedent(
        """
        import { searchMatrix } from './full_solution';

        const matrix = [
          [1, 3, 5],
          [7, 9, 11],
          [13, 15, 17],
        ];

        test('finds existing value', () => {
          expect(searchMatrix(matrix, 9)).toBe(true);
        });

        test('returns false for missing value', () => {
          expect(searchMatrix(matrix, 10)).toBe(false);
        });

        test('handles empty matrix', () => {
          expect(searchMatrix([], 1)).toBe(false);
        });
        """
    ),
)
add_task(
    id="task-028",
    category="sorting_search",
    function_name="partitionByPivot",
    docstring=dedent(
        """
        Implement `partitionByPivot` to reorder an array of numbers around a pivot value.
        Elements less than the pivot should come first, followed by elements equal to the pivot, then greater than the pivot.
        Return a new array reflecting the partition while preserving the relative order within each group.
        """
    ),
    readme=dedent(
        """
        # Description

        - **Domain:** sorting/search
        - Write `partitionByPivot(values: number[], pivot: number): number[]` to partition numbers around `pivot` while keeping relative order within groups.
        - Return a newly arranged array without mutating the input.
        """
    ),
    solution=dedent(
        """
        export function partitionByPivot(values: number[], pivot: number): number[] {
          // __FIM_HOLE_START__
          const less: number[] = [];
          const equal: number[] = [];
          const greater: number[] = [];

          for (const value of values) {
            if (value < pivot) {
              less.push(value);
            } else if (value > pivot) {
              greater.push(value);
            } else {
              equal.push(value);
            }
          }

          return [...less, ...equal, ...greater];
          // __FIM_HOLE_END__
        }
        """
    ),
    tests=dedent(
        """
        import { partitionByPivot } from './full_solution';

        test('orders values around pivot', () => {
          expect(partitionByPivot([3, 5, 2, 5, 1], 5)).toEqual([3, 2, 1, 5, 5]);
        });

        test('preserves relative order within groups', () => {
          expect(partitionByPivot([1, 2, 3, 4], 3)).toEqual([1, 2, 3, 4]);
        });

        test('handles no pivot matches', () => {
          expect(partitionByPivot([1, 2, 3], 0)).toEqual([1, 2, 3]);
        });
        """
    ),
)
add_task(
    id="task-029",
    category="sorting_search",
    function_name="countingSort",
    docstring=dedent(
        """
        Implement `countingSort` to sort an array of non-negative integers using the counting sort algorithm.
        Return a new sorted array without mutating the input.
        Throw an error if a negative number is encountered.
        """
    ),
    readme=dedent(
        """
        # Description

        - **Domain:** sorting/search
        - Create `countingSort(values: number[]): number[]` that sorts non-negative integers via counting sort.
        - Validate inputs to ensure no negatives are present and return a sorted copy of the data.
        """
    ),
    solution=dedent(
        """
        export function countingSort(values: number[]): number[] {
          // __FIM_HOLE_START__
          if (values.length === 0) {
            return [];
          }

          let max = 0;
          for (const value of values) {
            if (value < 0) {
              throw new Error('countingSort only accepts non-negative integers');
            }
            if (value > max) {
              max = value;
            }
          }

          const counts = new Array<number>(max + 1).fill(0);
          for (const value of values) {
            counts[value] += 1;
          }

          const result: number[] = [];
          counts.forEach((count, number) => {
            for (let i = 0; i < count; i += 1) {
              result.push(number);
            }
          });

          return result;
          // __FIM_HOLE_END__
        }
        """
    ),
    tests=dedent(
        """
        import { countingSort } from './full_solution';

        test('sorts non-negative integers', () => {
          expect(countingSort([3, 1, 2, 1])).toEqual([1, 1, 2, 3]);
        });

        test('handles empty array', () => {
          expect(countingSort([])).toEqual([]);
        });

        test('throws on negative input', () => {
          expect(() => countingSort([1, -1])).toThrow('countingSort only accepts non-negative integers');
        });
        """
    ),
)
add_task(
    id="task-030",
    category="sorting_search",
    function_name="interpolationSearch",
    docstring=dedent(
        """
        Implement `interpolationSearch` to search for a target within a sorted array of uniformly distributed numbers.
        Use the interpolation search formula to estimate the position and return the index of the target or `-1` when absent.
        Handle cases where the range collapses to avoid division by zero.
        """
    ),
    readme=dedent(
        """
        # Description

        - **Domain:** sorting/search
        - Write `interpolationSearch(values: number[], target: number): number` to locate a value in a sorted numeric array using interpolation search.
        - Return the index if found or `-1` otherwise, guarding against zero range divisions.
        """
    ),
    solution=dedent(
        """
        export function interpolationSearch(values: number[], target: number): number {
          // __FIM_HOLE_START__
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
          // __FIM_HOLE_END__
        }
        """
    ),
    tests=dedent(
        """
        import { interpolationSearch } from './full_solution';

        const values = [10, 20, 30, 40, 50, 60, 70];

        test('finds existing value', () => {
          expect(interpolationSearch(values, 50)).toBe(4);
        });

        test('returns -1 for missing value', () => {
          expect(interpolationSearch(values, 55)).toBe(-1);
        });

        test('handles uniform values', () => {
          expect(interpolationSearch([5, 5, 5, 5], 5)).toBe(0);
        });
        """
    ),
)
add_task(
    id="task-031",
    category="object",
    function_name="deepClone",
    docstring=dedent(
        """
        Implement `deepClone` to create a deep copy of plain objects and arrays.
        The function should recursively clone nested arrays and objects, and copy `Date` instances by value.
        Primitive values should be returned as-is.
        """
    ),
    readme=dedent(
        """
        # Description

        - **Domain:** object
        - Write `deepClone<T>(value: T): T` to deeply clone arrays, plain objects, and `Date` instances.
        - Preserve primitive values by returning them directly.
        """
    ),
    solution=dedent(
        """
        export function deepClone<T>(value: T): T {
          // __FIM_HOLE_START__
          if (value instanceof Date) {
            return new Date(value.getTime()) as T;
          }

          if (Array.isArray(value)) {
            return value.map((item) => deepClone(item)) as unknown as T;
          }

          if (value !== null && typeof value === 'object') {
            const result: Record<string, unknown> = {};
            for (const [key, val] of Object.entries(value as Record<string, unknown>)) {
              result[key] = deepClone(val);
            }
            return result as T;
          }

          return value;
          // __FIM_HOLE_END__
        }
        """
    ),
    tests=dedent(
        """
        import { deepClone } from './full_solution';

        test('clones nested objects', () => {
          const original = { a: { b: 1 } };
          const copy = deepClone(original);
          expect(copy).toEqual(original);
          expect(copy).not.toBe(original);
          expect(copy.a).not.toBe(original.a);
        });

        test('clones arrays', () => {
          const original = [1, [2, 3]];
          const copy = deepClone(original);
          expect(copy).toEqual(original);
          expect(copy[1]).not.toBe(original[1]);
        });

        test('clones dates', () => {
          const date = new Date();
          const copy = deepClone(date);
          expect(copy).not.toBe(date);
          expect(copy.getTime()).toBe(date.getTime());
        });
        """
    ),
)
add_task(
    id="task-032",
    category="object",
    function_name="deepMerge",
    docstring=dedent(
        """
        Implement `deepMerge` to merge two plain objects recursively.
        When both objects contain the same key with plain object values, merge them; when both are arrays, concatenate copies of the arrays.
        Other values should be overwritten by the source.
        """
    ),
    readme=dedent(
        """
        # Description

        - **Domain:** object
        - Write `deepMerge<T extends Record<string, unknown>, U extends Record<string, unknown>>(target: T, source: U): T & U` to recursively merge plain objects.
        - Concatenate arrays and clone nested objects to avoid mutating inputs.
        """
    ),
    solution=dedent(
        """
        const isPlainObject = (value: unknown): value is Record<string, unknown> =>
          value !== null && typeof value === 'object' && !Array.isArray(value) && !(value instanceof Date);

        export function deepMerge<T extends Record<string, unknown>, U extends Record<string, unknown>>(target: T, source: U): T & U {
          // __FIM_HOLE_START__
          const result: Record<string, unknown> = { ...target };

          for (const [key, sourceValue] of Object.entries(source)) {
            const targetValue = result[key];

            if (Array.isArray(targetValue) && Array.isArray(sourceValue)) {
              result[key] = [...targetValue, ...sourceValue.map((item) => (isPlainObject(item) ? deepMerge({}, item) : item))];
              continue;
            }

            if (isPlainObject(targetValue) && isPlainObject(sourceValue)) {
              result[key] = deepMerge(targetValue, sourceValue);
              continue;
            }

            result[key] = isPlainObject(sourceValue) ? deepMerge({}, sourceValue) : Array.isArray(sourceValue)
              ? sourceValue.slice()
              : sourceValue;
          }

          return result as T & U;
          // __FIM_HOLE_END__
        }
        """
    ),
    tests=dedent(
        """
        import { deepMerge } from './full_solution';

        test('merges nested objects', () => {
          const merged = deepMerge({ a: { b: 1 } }, { a: { c: 2 } });
          expect(merged).toEqual({ a: { b: 1, c: 2 } });
        });

        test('concatenates arrays', () => {
          const merged = deepMerge({ tags: ['a'] }, { tags: ['b'] });
          expect(merged.tags).toEqual(['a', 'b']);
        });

        test('overwrites primitive values', () => {
          expect(deepMerge({ count: 1 }, { count: 2 })).toEqual({ count: 2 });
        });
        """
    ),
)
add_task(
    id="task-033",
    category="object",
    function_name="groupByKey",
    docstring=dedent(
        """
        Implement `groupByKey` to group an array of records by the value of a specified key.
        Return a mapping from key values to arrays of records sharing that value.
        The original array should not be mutated.
        """
    ),
    readme=dedent(
        """
        # Description

        - **Domain:** object
        - Write `groupByKey<T extends Record<string, unknown>, K extends keyof T>(items: T[], key: K): Record<string, T[]>` to group records by `key`.
        - Convert grouping keys to strings to use as object keys and avoid mutating the input array.
        """
    ),
    solution=dedent(
        """
        export function groupByKey<T extends Record<string, unknown>, K extends keyof T>(items: T[], key: K): Record<string, T[]> {
          // __FIM_HOLE_START__
          return items.reduce<Record<string, T[]>>((groups, item) => {
            const groupKey = String(item[key]);
            if (!groups[groupKey]) {
              groups[groupKey] = [];
            }
            groups[groupKey].push(item);
            return groups;
          }, {});
          // __FIM_HOLE_END__
        }
        """
    ),
    tests=dedent(
        """
        import { groupByKey } from './full_solution';

        interface User {
          role: string;
          name: string;
        }

        const users: User[] = [
          { role: 'admin', name: 'A' },
          { role: 'user', name: 'B' },
          { role: 'admin', name: 'C' },
        ];

        test('groups by role', () => {
          expect(groupByKey(users, 'role')).toEqual({
            admin: [users[0], users[2]],
            user: [users[1]],
          });
        });

        test('handles empty array', () => {
          expect(groupByKey([], 'role')).toEqual({});
        });

        test('stringifies non-string keys', () => {
          expect(groupByKey([{ id: 1 }, { id: 1 }, { id: 2 }], 'id')).toEqual({ '1': [{ id: 1 }, { id: 1 }], '2': [{ id: 2 }] });
        });
        """
    ),
)
add_task(
    id="task-034",
    category="object",
    function_name="mapKeys",
    docstring=dedent(
        """
        Implement `mapKeys` to transform the keys of an object using a mapping function.
        The mapper receives the original key and value and returns a new key; the values remain unchanged.
        When multiple keys map to the same result, later keys should overwrite earlier ones.
        """
    ),
    readme=dedent(
        """
        # Description

        - **Domain:** object
        - Write `mapKeys<T extends Record<string, unknown>>(source: T, mapper: (key: keyof T, value: T[keyof T]) => string): Record<string, T[keyof T]>` to remap object keys.
        - Preserve values as-is and allow later keys to overwrite earlier collisions.
        """
    ),
    solution=dedent(
        """
        export function mapKeys<T extends Record<string, unknown>>(source: T, mapper: (key: keyof T, value: T[keyof T]) => string): Record<string, T[keyof T]> {
          // __FIM_HOLE_START__
          const result: Record<string, T[keyof T]> = {};
          (Object.keys(source) as Array<keyof T>).forEach((key) => {
            const newKey = mapper(key, source[key]);
            result[newKey] = source[key];
          });
          return result;
          // __FIM_HOLE_END__
        }
        """
    ),
    tests=dedent(
        """
        import { mapKeys } from './full_solution';

        test('renames keys with mapper', () => {
          const result = mapKeys({ firstName: 'Ada', lastName: 'Lovelace' }, (key) => key.toUpperCase());
          expect(result).toEqual({ FIRSTNAME: 'Ada', LASTNAME: 'Lovelace' });
        });

        test('handles key collisions by overwriting', () => {
          const result = mapKeys({ a: 1, b: 2 }, () => 'same');
          expect(result).toEqual({ same: 2 });
        });

        test('works with empty objects', () => {
          expect(mapKeys({}, (key) => String(key))).toEqual({});
        });
        """
    ),
)
add_task(
    id="task-035",
    category="object",
    function_name="omitKeys",
    docstring=dedent(
        """
        Implement `omitKeys` to produce a shallow copy of an object without specific keys.
        Accept the source object and an array of keys to remove.
        Return a new object excluding those keys without modifying the original.
        """
    ),
    readme=dedent(
        """
        # Description

        - **Domain:** object
        - Write `omitKeys<T extends Record<string, unknown>, K extends keyof T>(source: T, keys: K[]): Omit<T, K>` to remove selected keys from an object copy.
        - Do not mutate the original object.
        """
    ),
    solution=dedent(
        """
        export function omitKeys<T extends Record<string, unknown>, K extends keyof T>(source: T, keys: K[]): Omit<T, K> {
          // __FIM_HOLE_START__
          const exclusions = new Set(keys);
          const result: Record<string, unknown> = {};

          (Object.keys(source) as Array<keyof T>).forEach((key) => {
            if (!exclusions.has(key)) {
              result[key as string] = source[key];
            }
          });

          return result as Omit<T, K>;
          // __FIM_HOLE_END__
        }
        """
    ),
    tests=dedent(
        """
        import { omitKeys } from './full_solution';

        test('omits specified keys', () => {
          expect(omitKeys({ a: 1, b: 2, c: 3 }, ['b'])).toEqual({ a: 1, c: 3 });
        });

        test('handles empty keys array', () => {
          expect(omitKeys({ a: 1 }, [])).toEqual({ a: 1 });
        });

        test('ignores keys not present', () => {
          expect(omitKeys<Record<string, number>, string>({ a: 1 }, ['missing'])).toEqual({ a: 1 });
        });
        """
    ),
)
add_task(
    id="task-036",
    category="object",
    function_name="getValueByPath",
    docstring=dedent(
        """
        Implement `getValueByPath` to retrieve a nested value from an object using a dot-separated path.
        If any segment is missing, return `undefined`.
        Treat array indices as numeric segments in the path.
        """
    ),
    readme=dedent(
        """
        # Description

        - **Domain:** object
        - Write `getValueByPath(source: unknown, path: string): unknown` to resolve nested properties with dot notation (e.g., `user.address.city`).
        - Interpret numeric segments as array indices and return `undefined` when traversal fails.
        """
    ),
    solution=dedent(
        """
        export function getValueByPath(source: unknown, path: string): unknown {
          // __FIM_HOLE_START__
          if (!path) {
            return source;
          }

          const segments = path.split('.');
          let current: unknown = source;

          for (const segment of segments) {
            if (current === null || typeof current !== 'object') {
              return undefined;
            }

            if (Array.isArray(current) && /^\d+$/.test(segment)) {
              current = current[Number(segment)];
            } else {
              current = (current as Record<string, unknown>)[segment];
            }
          }

          return current;
          // __FIM_HOLE_END__
        }
        """
    ),
    tests=dedent(
        """
        import { getValueByPath } from './full_solution';

        const data = { user: { address: { city: 'Paris' } }, items: [{ name: 'Book' }] };

        test('retrieves nested value', () => {
          expect(getValueByPath(data, 'user.address.city')).toBe('Paris');
        });

        test('handles array indices', () => {
          expect(getValueByPath(data, 'items.0.name')).toBe('Book');
        });

        test('returns undefined when path missing', () => {
          expect(getValueByPath(data, 'user.address.zip')).toBeUndefined();
        });
        """
    ),
)
add_task(
    id="task-037",
    category="object",
    function_name="setValueByPath",
    docstring=dedent(
        """
        Implement `setValueByPath` to set a value on a nested object or array using a dot-separated path.
        Create intermediate objects or arrays as needed and return a new cloned structure leaving the original untouched.
        Numeric path segments should create arrays.
        """
    ),
    readme=dedent(
        """
        # Description

        - **Domain:** object
        - Write `setValueByPath<T extends Record<string, unknown>>(source: T, path: string, value: unknown): T & Record<string, unknown>` to assign a nested value.
        - Generate intermediate containers without mutating `source`, interpreting numeric segments as array indices.
        """
    ),
    solution=dedent(
        """
        const cloneStructure = (input: unknown): unknown => {
          if (Array.isArray(input)) {
            return input.map((item) => cloneStructure(item));
          }
          if (input !== null && typeof input === 'object') {
            const result: Record<string, unknown> = {};
            for (const [key, value] of Object.entries(input as Record<string, unknown>)) {
              result[key] = cloneStructure(value);
            }
            return result;
          }
          return input;
        };

        const isNumericSegment = (segment: string): boolean => /^\d+$/.test(segment);

        export function setValueByPath<T extends Record<string, unknown>>(source: T, path: string, value: unknown): T & Record<string, unknown> {
          // __FIM_HOLE_START__
          if (!path) {
            return cloneStructure(value) as T & Record<string, unknown>;
          }

          const clone = cloneStructure(source) as Record<string, unknown> | unknown[];
          const segments = path.split('.');
          let current: any = clone;

          for (let index = 0; index < segments.length; index += 1) {
            const segment = segments[index];
            const isLast = index === segments.length - 1;
            const key = isNumericSegment(segment) ? Number(segment) : segment;

            if (isLast) {
              if (Array.isArray(current) && typeof key === 'number') {
                current[key] = cloneStructure(value);
              } else {
                current[key] = cloneStructure(value);
              }
              break;
            }

            const nextSegment = segments[index + 1];
            const shouldCreateArray = isNumericSegment(nextSegment);

            if (current[key] === undefined || current[key] === null || typeof current[key] !== 'object') {
              current[key] = shouldCreateArray ? [] : {};
            } else {
              current[key] = cloneStructure(current[key]);
            }

            current = current[key];
          }

          return clone as T & Record<string, unknown>;
          // __FIM_HOLE_END__
        }
        """
    ),
    tests=dedent(
        """
        import { setValueByPath } from './full_solution';

        test('sets nested value on new object', () => {
          const result = setValueByPath({}, 'user.name', 'Ada');
          expect(result).toEqual({ user: { name: 'Ada' } });
        });

        test('creates arrays for numeric segments', () => {
          const result = setValueByPath({}, 'items.0.name', 'Book');
          expect(Array.isArray((result as any).items)).toBe(true);
          expect((result as any).items[0]).toEqual({ name: 'Book' });
        });

        test('does not mutate source', () => {
          const source = { user: { name: 'Ada' } };
          const result = setValueByPath(source, 'user.name', 'Grace');
          expect(source.user?.name).toBe('Ada');
          expect(result.user?.name).toBe('Grace');
        });
        """
    ),
)
add_task(
    id="task-038",
    category="object",
    function_name="diffObjects",
    docstring=dedent(
        """
        Implement `diffObjects` to compare two plain objects and describe their differences.
        Return a mapping from keys to `{ before, after }` pairs for keys whose values are not strictly equal.
        Include keys present in one object but not the other.
        """
    ),
    readme=dedent(
        """
        # Description

        - **Domain:** object
        - Write `diffObjects<T extends Record<string, unknown>>(previous: T, next: T): Record<string, { before: unknown; after: unknown }>` to capture differences between two objects.
        - Use strict equality to compare values and include added or removed keys.
        """
    ),
    solution=dedent(
        """
        export function diffObjects<T extends Record<string, unknown>>(previous: T, next: T): Record<string, { before: unknown; after: unknown }> {
          // __FIM_HOLE_START__
          const diff: Record<string, { before: unknown; after: unknown }> = {};
          const keys = new Set([...Object.keys(previous), ...Object.keys(next)]);

          keys.forEach((key) => {
            const before = previous[key as keyof T];
            const after = next[key as keyof T];
            if (before !== after) {
              diff[key] = { before, after };
            }
          });

          return diff;
          // __FIM_HOLE_END__
        }
        """
    ),
    tests=dedent(
        """
        import { diffObjects } from './full_solution';

        test('detects updated values', () => {
          expect(diffObjects({ a: 1 }, { a: 2 })).toEqual({ a: { before: 1, after: 2 } });
        });

        test('detects removed keys', () => {
          expect(diffObjects({ a: 1 }, {})).toEqual({ a: { before: 1, after: undefined } });
        });

        test('detects added keys', () => {
          expect(diffObjects({}, { b: 2 })).toEqual({ b: { before: undefined, after: 2 } });
        });
        """
    ),
)
add_task(
    id="task-039",
    category="object",
    function_name="filterObject",
    docstring=dedent(
        """
        Implement `filterObject` to produce a new object containing only entries that satisfy a predicate.
        The predicate receives the value and key and should return a boolean indicating whether to keep the pair.
        The original object must remain unchanged.
        """
    ),
    readme=dedent(
        """
        # Description

        - **Domain:** object
        - Write `filterObject<T extends Record<string, unknown>>(source: T, predicate: (value: T[keyof T], key: keyof T) => boolean): Partial<T>` to filter entries.
        - Preserve the original object and include entries in the same iteration order.
        """
    ),
    solution=dedent(
        """
        export function filterObject<T extends Record<string, unknown>>(source: T, predicate: (value: T[keyof T], key: keyof T) => boolean): Partial<T> {
          // __FIM_HOLE_START__
          const result: Partial<T> = {};
          (Object.keys(source) as Array<keyof T>).forEach((key) => {
            const value = source[key];
            if (predicate(value, key)) {
              result[key] = value;
            }
          });
          return result;
          // __FIM_HOLE_END__
        }
        """
    ),
    tests=dedent(
        """
        import { filterObject } from './full_solution';

        test('filters values based on predicate', () => {
          expect(filterObject({ a: 1, b: 2, c: 3 }, (value) => value > 1)).toEqual({ b: 2, c: 3 });
        });

        test('returns empty object when nothing matches', () => {
          expect(filterObject({ a: 1 }, () => false)).toEqual({});
        });

        test('passes key to predicate', () => {
          const result = filterObject({ keep: true, drop: false }, (_value, key) => key === 'keep');
          expect(result).toEqual({ keep: true });
        });
        """
    ),
)
add_task(
    id="task-040",
    category="object",
    function_name="invertObject",
    docstring=dedent(
        """
        Implement `invertObject` to swap keys and values of an object.
        The input object's values must be convertible to strings to become keys in the result.
        When duplicate values occur, later keys should overwrite earlier ones.
        """
    ),
    readme=dedent(
        """
        # Description

        - **Domain:** object
        - Write `invertObject(source: Record<string, string | number | boolean>): Record<string, string>` to invert keys and values.
        - Convert values to strings for use as keys, with later entries taking precedence on collisions.
        """
    ),
    solution=dedent(
        """
        export function invertObject(source: Record<string, string | number | boolean>): Record<string, string> {
          // __FIM_HOLE_START__
          const result: Record<string, string> = {};
          Object.entries(source).forEach(([key, value]) => {
            result[String(value)] = key;
          });
          return result;
          // __FIM_HOLE_END__
        }
        """
    ),
    tests=dedent(
        """
        import { invertObject } from './full_solution';

        test('inverts keys and values', () => {
          expect(invertObject({ a: 'x', b: 'y' })).toEqual({ x: 'a', y: 'b' });
        });

        test('stringifies non-string values', () => {
          expect(invertObject({ a: 1, b: true })).toEqual({ '1': 'a', true: 'b' });
        });

        test('later values overwrite earlier ones', () => {
          expect(invertObject({ a: 'x', b: 'x' })).toEqual({ x: 'b' });
        });
        """
    ),
)
add_task(
    id="task-041",
    category="async",
    function_name="retryAsync",
    docstring=dedent(
        """
        Implement `retryAsync` to repeatedly invoke an asynchronous operation until it succeeds or the retry limit is reached.
        Accept an operation returning a promise, the maximum number of attempts, and an optional delay in milliseconds between attempts.
        Reject with the last error when all attempts fail.
        """
    ),
    readme=dedent(
        """
        # Description

        - **Domain:** async
        - Write `retryAsync<T>(operation: () => Promise<T>, attempts: number, delayMs?: number): Promise<T>` to retry failed operations.
        - Wait `delayMs` milliseconds between attempts (default 0) and reject with the last error if all retries fail.
        """
    ),
    solution=dedent(
        """
        const wait = (ms: number): Promise<void> => new Promise((resolve) => setTimeout(resolve, ms));

        export async function retryAsync<T>(operation: () => Promise<T>, attempts: number, delayMs = 0): Promise<T> {
          // __FIM_HOLE_START__
          if (attempts <= 0) {
            throw new Error('attempts must be greater than 0');
          }

          let lastError: unknown;
          for (let attempt = 1; attempt <= attempts; attempt += 1) {
            try {
              return await operation();
            } catch (error) {
              lastError = error;
              if (attempt < attempts && delayMs > 0) {
                await wait(delayMs);
              }
            }
          }

          throw lastError instanceof Error ? lastError : new Error('Operation failed');
          // __FIM_HOLE_END__
        }
        """
    ),
    tests=dedent(
        """
        import { retryAsync } from './full_solution';

        test('retries until success', async () => {
          let attempts = 0;
          const result = await retryAsync(async () => {
            attempts += 1;
            if (attempts < 3) {
              throw new Error('fail');
            }
            return 'ok';
          }, 5);
          expect(result).toBe('ok');
          expect(attempts).toBe(3);
        });

        test('throws after exhausting attempts', async () => {
          await expect(
            retryAsync(
              async () => {
                throw new Error('always fails');
              },
              2,
            ),
          ).rejects.toThrow('always fails');
        });

        test('handles zero delay gracefully', async () => {
          let count = 0;
          await expect(
            retryAsync(
              async () => {
                count += 1;
                throw new Error('nope');
              },
              1,
            ),
          ).rejects.toThrow('nope');
          expect(count).toBe(1);
        });
        """
    ),
)
add_task(
    id="task-042",
    category="async",
    function_name="withTimeout",
    docstring=dedent(
        """
        Implement `withTimeout` to wrap a promise with a timeout.
        If the wrapped promise does not settle within the specified milliseconds, reject with a timeout error message.
        Allow a custom error message, defaulting to `"Operation timed out"`.
        """
    ),
    readme=dedent(
        """
        # Description

        - **Domain:** async
        - Write `withTimeout<T>(promise: Promise<T>, timeoutMs: number, message?: string): Promise<T>` to enforce a timeout on a promise.
        - Reject with a timeout error message when the promise does not settle in time.
        """
    ),
    solution=dedent(
        """
        export function withTimeout<T>(promise: Promise<T>, timeoutMs: number, message = 'Operation timed out'): Promise<T> {
          // __FIM_HOLE_START__
          return new Promise<T>((resolve, reject) => {
            const timer = setTimeout(() => {
              reject(new Error(message));
            }, timeoutMs);

            promise
              .then((value) => {
                clearTimeout(timer);
                resolve(value);
              })
              .catch((error) => {
                clearTimeout(timer);
                reject(error);
              });
          });
          // __FIM_HOLE_END__
        }
        """
    ),
    tests=dedent(
        """
        import { withTimeout } from './full_solution';

        test('resolves before timeout', async () => {
          const result = await withTimeout(Promise.resolve('done'), 50);
          expect(result).toBe('done');
        });

        test('rejects after timeout', async () => {
          await expect(
            withTimeout(
              new Promise<void>((resolve) => setTimeout(resolve, 30)),
              10,
            ),
          ).rejects.toThrow('Operation timed out');
        });

        test('uses custom message', async () => {
          await expect(withTimeout(new Promise<void>(() => {}), 5, 'Too slow')).rejects.toThrow('Too slow');
        });
        """
    ),
)
add_task(
    id="task-043",
    category="async",
    function_name="pollUntil",
    docstring=dedent(
        """
        Implement `pollUntil` to repeatedly invoke an asynchronous factory until a predicate returns true or a timeout expires.
        Accept a polling interval in milliseconds and a total timeout duration.
        Reject with an error when the timeout is reached without satisfying the predicate.
        """
    ),
    readme=dedent(
        """
        # Description

        - **Domain:** async
        - Write `pollUntil<T>(factory: () => Promise<T>, predicate: (value: T) => boolean, intervalMs: number, timeoutMs: number): Promise<T>`.
        - Resolve with the first value that satisfies the predicate or reject when the timeout elapses.
        """
    ),
    solution=dedent(
        """
        const sleep = (ms: number): Promise<void> => new Promise((resolve) => setTimeout(resolve, ms));

        export async function pollUntil<T>(
          factory: () => Promise<T>,
          predicate: (value: T) => boolean,
          intervalMs: number,
          timeoutMs: number,
        ): Promise<T> {
          // __FIM_HOLE_START__
          const deadline = Date.now() + timeoutMs;

          while (true) {
            const result = await factory();
            if (predicate(result)) {
              return result;
            }

            if (Date.now() >= deadline) {
              throw new Error('Polling timed out');
            }

            if (intervalMs > 0) {
              const waitTime = Math.min(intervalMs, Math.max(0, deadline - Date.now()));
              if (waitTime > 0) {
                await sleep(waitTime);
              }
            }
          }
          // __FIM_HOLE_END__
        }
        """
    ),
    tests=dedent(
        """
        import { pollUntil } from './full_solution';

        test('resolves when predicate eventually matches', async () => {
          let count = 0;
          const result = await pollUntil(
            async () => {
              count += 1;
              return count;
            },
            (value) => value >= 3,
            0,
            50,
          );
          expect(result).toBe(3);
        });

        test('rejects on timeout', async () => {
          await expect(
            pollUntil(
              async () => 0,
              (value) => value === 1,
              5,
              20,
            ),
          ).rejects.toThrow('Polling timed out');
        });

        test('waits between attempts when interval provided', async () => {
          const start = Date.now();
          let count = 0;
          await pollUntil(
            async () => {
              count += 1;
              return count;
            },
            (value) => value >= 2,
            10,
            100,
          );
          expect(Date.now() - start).toBeGreaterThanOrEqual(10);
        });
        """
    ),
)
add_task(
    id="task-044",
    category="async",
    function_name="limitConcurrency",
    docstring=dedent(
        """
        Implement `limitConcurrency` to execute asynchronous tasks with a maximum number of concurrent operations.
        Accept an array of functions returning promises and a positive concurrency limit.
        Resolve with an array of results preserving the order of the original tasks.
        """
    ),
    readme=dedent(
        """
        # Description

        - **Domain:** async
        - Write `limitConcurrency<T>(tasks: Array<() => Promise<T>>, limit: number): Promise<T[]>` to run tasks under a concurrency cap.
        - Preserve result order and reject immediately if any task rejects.
        """
    ),
    solution=dedent(
        """
        export async function limitConcurrency<T>(tasks: Array<() => Promise<T>>, limit: number): Promise<T[]> {
          // __FIM_HOLE_START__
          if (limit <= 0) {
            throw new Error('limit must be greater than 0');
          }

          const results: T[] = new Array(tasks.length);
          let index = 0;

          const workers: Promise<void>[] = [];

          const runNext = async (): Promise<void> => {
            const currentIndex = index;
            index += 1;
            if (currentIndex >= tasks.length) {
              return;
            }
            const task = tasks[currentIndex];
            results[currentIndex] = await task();
            await runNext();
          };

          for (let i = 0; i < Math.min(limit, tasks.length); i += 1) {
            workers.push(runNext());
          }

          await Promise.all(workers);
          return results;
          // __FIM_HOLE_END__
        }
        """
    ),
    tests=dedent(
        """
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
        """
    ),
)
add_task(
    id="task-045",
    category="async",
    function_name="batchPromises",
    docstring=dedent(
        """
        Implement `batchPromises` to process an array of items in batches using an asynchronous mapper.
        Execute each batch sequentially while awaiting all promises within the batch in parallel.
        Preserve the order of results matching the input items.
        """
    ),
    readme=dedent(
        """
        # Description

        - **Domain:** async
        - Write `batchPromises<T, R>(items: T[], batchSize: number, mapper: (item: T, index: number) => Promise<R>): Promise<R[]>`.
        - Run up to `batchSize` asynchronous operations at once, processing batches sequentially.
        """
    ),
    solution=dedent(
        """
        export async function batchPromises<T, R>(
          items: T[],
          batchSize: number,
          mapper: (item: T, index: number) => Promise<R>,
        ): Promise<R[]> {
          // __FIM_HOLE_START__
          if (batchSize <= 0) {
            throw new Error('batchSize must be greater than 0');
          }

          const results: R[] = [];

          for (let i = 0; i < items.length; i += batchSize) {
            const batch = items.slice(i, i + batchSize).map((item, offset) => mapper(item, i + offset));
            const batchResults = await Promise.all(batch);
            results.push(...batchResults);
          }

          return results;
          // __FIM_HOLE_END__
        }
        """
    ),
    tests=dedent(
        """
        import { batchPromises } from './full_solution';

        test('processes items in batches', async () => {
          const order: number[] = [];
          const results = await batchPromises([1, 2, 3, 4], 2, async (value) => {
            order.push(value);
            return value * 2;
          });
          expect(results).toEqual([2, 4, 6, 8]);
          expect(order).toEqual([1, 2, 3, 4]);
        });

        test('handles empty list', async () => {
          const results = await batchPromises([], 3, async (value) => value);
          expect(results).toEqual([]);
        });

        test('throws on invalid batch size', async () => {
          await expect(batchPromises([1], 0, async (value) => value)).rejects.toThrow('batchSize must be greater than 0');
        });
        """
    ),
)
add_task(
    id="task-046",
    category="async",
    function_name="runSequentially",
    docstring=dedent(
        """
        Implement `runSequentially` to execute an array of asynchronous functions one after another.
        Each function returns a promise whose resolution should be awaited before starting the next.
        Resolve with an array of the fulfilled values in order.
        """
    ),
    readme=dedent(
        """
        # Description

        - **Domain:** async
        - Write `runSequentially<T>(tasks: Array<() => Promise<T>>): Promise<T[]>` to chain asynchronous tasks sequentially.
        - Await each task before invoking the next and collect their results in order.
        """
    ),
    solution=dedent(
        """
        export async function runSequentially<T>(tasks: Array<() => Promise<T>>): Promise<T[]> {
          // __FIM_HOLE_START__
          const results: T[] = [];
          for (const task of tasks) {
            results.push(await task());
          }
          return results;
          // __FIM_HOLE_END__
        }
        """
    ),
    tests=dedent(
        """
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
        """
    ),
)
add_task(
    id="task-047",
    category="async",
    function_name="fetchWithFallback",
    docstring=dedent(
        """
        Implement `fetchWithFallback` to attempt fetching a resource from multiple URLs until one succeeds.
        Accept an array of URLs and a fetch-like function returning a promise of a response with an `ok` boolean.
        Resolve with the first successful response or reject with the last error when all attempts fail.
        """
    ),
    readme=dedent(
        """
        # Description

        - **Domain:** async
        - Write `fetchWithFallback(urls: string[], fetcher: (url: string) => Promise<{ ok: boolean }>): Promise<{ ok: boolean }>`.
        - Try each URL in order until `ok` is true; otherwise reject with the last error encountered.
        """
    ),
    solution=dedent(
        """
        export interface FetchLikeResponse {
          ok: boolean;
        }

        export async function fetchWithFallback(
          urls: string[],
          fetcher: (url: string) => Promise<FetchLikeResponse>,
        ): Promise<FetchLikeResponse> {
          // __FIM_HOLE_START__
          if (urls.length === 0) {
            throw new Error('No URLs provided');
          }

          let lastError: unknown;
          for (const url of urls) {
            try {
              const response = await fetcher(url);
              if (response.ok) {
                return response;
              }
              lastError = new Error(`Request to ${url} failed`);
            } catch (error) {
              lastError = error;
            }
          }

          throw lastError instanceof Error ? lastError : new Error('All fetch attempts failed');
          // __FIM_HOLE_END__
        }
        """
    ),
    tests=dedent(
        """
        import { fetchWithFallback } from './full_solution';

        test('returns first successful response', async () => {
          const calls: string[] = [];
          const response = await fetchWithFallback(
            ['a', 'b'],
            async (url) => {
              calls.push(url);
              if (url === 'b') {
                return { ok: true };
              }
              return { ok: false };
            },
          );
          expect(response.ok).toBe(true);
          expect(calls).toEqual(['a', 'b']);
        });

        test('rejects when all attempts fail', async () => {
          await expect(
            fetchWithFallback(
              ['a'],
              async () => {
                throw new Error('network');
              },
            ),
          ).rejects.toThrow('network');
        });

        test('throws when no urls provided', async () => {
          await expect(fetchWithFallback([], async () => ({ ok: true }))).rejects.toThrow('No URLs provided');
        });
        """
    ),
)
add_task(
    id="task-048",
    category="async",
    function_name="memoizeAsync",
    docstring=dedent(
        """
        Implement `memoizeAsync` to memoize an asynchronous function based on its arguments.
        Cache in-flight promises so concurrent calls with the same arguments share the result.
        Remove cache entries when the promise rejects to allow retries.
        """
    ),
    readme=dedent(
        """
        # Description

        - **Domain:** async
        - Write `memoizeAsync<T extends (...args: any[]) => Promise<any>>(fn: T): T` to memoize asynchronous functions.
        - Use JSON stringification of arguments as the cache key and reuse pending promises.
        """
    ),
    solution=dedent(
        """
        export function memoizeAsync<T extends (...args: any[]) => Promise<any>>(fn: T): T {
          // __FIM_HOLE_START__
          const cache = new Map<string, Promise<any>>();

          const memoized = (...args: Parameters<T>): ReturnType<T> => {
            const key = JSON.stringify(args);
            if (!cache.has(key)) {
              const promise = fn(...args)
                .then((result) => {
                  cache.set(key, Promise.resolve(result));
                  return result;
                })
                .catch((error) => {
                  cache.delete(key);
                  throw error;
                });
              cache.set(key, promise);
            }
            return cache.get(key)! as ReturnType<T>;
          };

          return memoized as T;
          // __FIM_HOLE_END__
        }
        """
    ),
    tests=dedent(
        """
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
        """
    ),
)
add_task(
    id="task-049",
    category="async",
    function_name="mapAsyncSeries",
    docstring=dedent(
        """
        Implement `mapAsyncSeries` to apply an asynchronous mapper to an array sequentially.
        Await each mapper invocation before proceeding to the next item.
        Return a promise that resolves with the array of mapped results in order.
        """
    ),
    readme=dedent(
        """
        # Description

        - **Domain:** async
        - Write `mapAsyncSeries<T, R>(items: T[], mapper: (item: T, index: number) => Promise<R>): Promise<R[]>` to map sequentially.
        - Ensure each item is processed after the previous one finishes.
        """
    ),
    solution=dedent(
        """
        export async function mapAsyncSeries<T, R>(items: T[], mapper: (item: T, index: number) => Promise<R>): Promise<R[]> {
          // __FIM_HOLE_START__
          const results: R[] = [];
          for (let index = 0; index < items.length; index += 1) {
            results.push(await mapper(items[index], index));
          }
          return results;
          // __FIM_HOLE_END__
        }
        """
    ),
    tests=dedent(
        """
        import { mapAsyncSeries } from './full_solution';

        test('maps sequentially', async () => {
          const order: number[] = [];
          const results = await mapAsyncSeries([1, 2, 3], async (value) => {
            order.push(value);
            return value * 2;
          });
          expect(results).toEqual([2, 4, 6]);
          expect(order).toEqual([1, 2, 3]);
        });

        test('handles empty array', async () => {
          expect(await mapAsyncSeries([], async (value) => value)).toEqual([]);
        });

        test('propagates errors', async () => {
          await expect(
            mapAsyncSeries([1, 2], async (value) => {
              if (value === 2) {
                throw new Error('fail');
              }
              return value;
            }),
          ).rejects.toThrow('fail');
        });
        """
    ),
)
add_task(
    id="task-050",
    category="async",
    function_name="makeCancelable",
    docstring=dedent(
        """
        Implement `makeCancelable` to create a cancellable promise wrapper around an asynchronous operation.
        Accept an executor that receives an `AbortSignal` and returns a promise.
        Provide a `cancel` function that aborts the signal and rejects the promise with `"Operation cancelled"` if it has not yet settled.
        """
    ),
    readme=dedent(
        """
        # Description

        - **Domain:** async
        - Write `makeCancelable<T>(executor: (signal: AbortSignal) => Promise<T>): { promise: Promise<T>; cancel: () => void }`.
        - Abort the underlying `AbortSignal` on cancel and reject with `Operation cancelled` when cancellation happens before resolution.
        """
    ),
    solution=dedent(
        """
        export interface CancelablePromise<T> {
          promise: Promise<T>;
          cancel: () => void;
        }

        export function makeCancelable<T>(executor: (signal: AbortSignal) => Promise<T>): CancelablePromise<T> {
          // __FIM_HOLE_START__
          const controller = new AbortController();
          let settled = false;
          let rejectPromise: ((reason?: unknown) => void) | undefined;

          const promise = new Promise<T>((resolve, reject) => {
            rejectPromise = reject;

            executor(controller.signal)
              .then((value) => {
                settled = true;
                resolve(value);
              })
              .catch((error) => {
                settled = true;
                reject(error);
              });

            controller.signal.addEventListener('abort', () => {
              if (!settled) {
                settled = true;
                reject(new Error('Operation cancelled'));
              }
            });
          });

          return {
            promise,
            cancel: () => {
              if (!controller.signal.aborted) {
                controller.abort();
                if (!settled && rejectPromise) {
                  rejectPromise(new Error('Operation cancelled'));
                }
              }
            },
          };
          // __FIM_HOLE_END__
        }
        """
    ),
    tests=dedent(
        """
        import { makeCancelable } from './full_solution';

        const delay = (ms: number): Promise<void> => new Promise((resolve) => setTimeout(resolve, ms));

        test('resolves normally when not cancelled', async () => {
          const { promise, cancel } = makeCancelable(async () => {
            await delay(5);
            return 'done';
          });
          const result = await promise;
          expect(result).toBe('done');
          cancel();
        });

        test('rejects when cancelled', async () => {
          const { promise, cancel } = makeCancelable(async (signal) => {
            while (!signal.aborted) {
              await delay(5);
            }
            return 'never';
          });
          const rejection = promise.catch((error) => error.message);
          cancel();
          expect(await rejection).toBe('Operation cancelled');
        });

        test('ignores cancel after resolution', async () => {
          const { promise, cancel } = makeCancelable(async () => 'instant');
          await expect(promise).resolves.toBe('instant');
          expect(() => cancel()).not.toThrow();
        });
        """
    ),
)

if __name__ == '__main__':
    main()
