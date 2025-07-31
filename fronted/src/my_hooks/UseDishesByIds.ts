import { useQuery } from "@tanstack/react-query";
import api from "./FastApiAxiosBaseUrl";

const useDishesByIds = (qids: string | null) => {
  const fetchData = async () => {
    try {
      const response = await api.get(`/dishes_by_r_id?id=${qids}`);

      return response.data;
    } catch (error) {
      throw error;
    }
  };

  return useQuery({
    queryKey: ["dishes", qids],
    queryFn: fetchData,
    enabled: !!qids,
    staleTime: 3600000,
    refetchOnWindowFocus: false,
  });
};

export default useDishesByIds;
