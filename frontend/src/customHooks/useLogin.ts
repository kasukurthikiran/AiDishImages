import { useMutation } from "@tanstack/react-query";
import api from "./useAxiosApi";

function useCustomPostLogin() {
  const mutationFn = async (data: any) => {
    const formData = new URLSearchParams();
    formData.append("username", data.username);
    formData.append("password", data.password);

    const response = await api.post("/token", formData, {
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
    });

    return response.data;
  };

  return useMutation({ mutationFn });
}

export default useCustomPostLogin;
