import { useEffect, useState } from "react";

export function usePolling<T>(
  fetchFn: () => Promise<T>,
  shouldPoll: boolean,
  intervalMs: number
) {
  const [data, setData] = useState<T | null>(null);

  const fetchData = async () => {
    try {
      const result = await fetchFn();
      setData(result);
    } catch (e) {
      console.error("Error in polling:", e);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);
  useEffect(() => {
    if (!shouldPoll) return;
    const intervalId = setInterval(fetchData, intervalMs);
    return () => clearInterval(intervalId);
  }, [shouldPoll]);
  return data;
}
