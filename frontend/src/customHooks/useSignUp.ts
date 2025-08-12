import { useMutation } from "@tanstack/react-query";
import api from "./useAxiosApi";

const useSignup = () => {
  const mutationFn = async (data: any) => {
    const response = await api.post("/register", data);
    return response.data;
  };

  return useMutation({ mutationFn });
};

export default useSignup;
