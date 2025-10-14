/* Docstring:
 * Implement `makeCancelable` to create a cancellable promise wrapper around an asynchronous operation.
 * Accept an executor that receives an `AbortSignal` and returns a promise.
 * Provide a `cancel` function that aborts the signal and rejects the promise with `"Operation cancelled"` if it has not yet settled.
 */
<｜fim▁begin｜>
export interface CancelablePromise<T> {
  promise: Promise<T>;
  cancel: () => void;
}

export function makeCancelable<T>(executor: (signal: AbortSignal) => Promise<T>): CancelablePromise<T> {
<｜fim▁hole｜>
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
<｜fim▁end｜>
}
