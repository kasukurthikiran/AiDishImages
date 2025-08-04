import { useQuery } from "@tanstack/react-query";
import api from "./useAxiosApi";

const UseAllDishes = () => {
  const fetchData = async () => {
    try {
      const response = await api.get(`/dishes_by_all_r_id`);

      return response.data;
    } catch (error) {
      throw error;
    }
  };

  return useQuery({
    queryKey: ["dishes"],
    queryFn: fetchData,
    enabled: true,
    staleTime: 3600000,
    refetchOnWindowFocus: false,
  });
};

export default UseAllDishes;
