import { useQuery } from "@tanstack/react-query";
import api from "./useAxiosApi";

const UseAllRestaurant = () => {
  const fetchData = async () => {
    try {
      const response = await api.get(`/restaurants_data`);

      return response.data;
    } catch (error) {
      throw error;
    }
  };

  return useQuery({
    queryKey: ["restaurants"],
    queryFn: fetchData,
    enabled: true,
    staleTime: 3600000,
    refetchOnWindowFocus: false,
  });
};

export default UseAllRestaurant;
