export interface CancelablePromise<T> {
  promise: Promise<T>;
  cancel: () => void;
}

export function makeCancelable<T>(executor: (signal: AbortSignal) => Promise<T>): CancelablePromise<T> {
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
}
