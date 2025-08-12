import { useQuery } from "@tanstack/react-query";
import api from "./useAxiosApi";

const useDishesByIds = (qids: string | null) => {
  const fetchData = async () => {
    const response = await api.get(`/dishes_by_r_id?id=${qids}`);
    console.log("i am from response", response);
    return response.data.dishes;
  };

  return useQuery({
    queryKey: ["dishes", qids],
    queryFn: fetchData,
    enabled: !!qids,
    staleTime: 3600000,
    refetchOnWindowFocus: false,
    refetchInterval: (data) => {
      const f_data = data.state.data;
      console.log("i am from refetch", data);
      console.log("i ", f_data);
      if (!f_data || !Array.isArray(f_data)) return false;
      const shouldPoll = f_data.some((dish: any) => dish.image_path === "");
      return shouldPoll ? 1000 : false;
    },
  });
};

export default useDishesByIds;
