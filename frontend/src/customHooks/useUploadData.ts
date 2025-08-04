import { useMutation } from "@tanstack/react-query";
import api from "./useAxiosApi";

const useUploadData = () => {
  const mutationFn = async (data: FormData) => {
    const response = await api.post("/upload/", data, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    });
    return response.data;
  };

  return useMutation({ mutationFn });
};

export default useUploadData;
