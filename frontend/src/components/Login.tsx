import { useEffect, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { Label } from "@radix-ui/react-label";
import { Input } from "./ui/input";
import { Button } from "./ui/button";
import useCustomPostLogin from "@/customHooks/useLogin";

function Login() {
  const [token, setToken] = useState(localStorage.getItem("token"));

  useEffect(() => {
    const handleStorageChange = () => {
      setToken(localStorage.getItem("token"));
    };

    window.addEventListener("storage", handleStorageChange);

    return () => {
      window.removeEventListener("storage", handleStorageChange);
    };
  }, [setToken]);

  const [Username, setUsername] = useState("");
  const [Password, setPassword] = useState("");
  const navigate = useNavigate();

  const { data, mutate, isPending } = useCustomPostLogin();

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    if (!Username || !Password) {
      alert("Please fill all fields.");
      return;
    }

    mutate(
      {
        username: Username,
        password: Password,
      },
      {
        onSuccess: (response) => {
          localStorage.setItem("token", response.access_token);
          console.log(response.access_token);
          alert("Login successful!");
          navigate("/home");
        },
        onError: (error) => {
          alert("Registration failed: " + error.response?.data?.detail);
        },
      }
    );
  };

  return (
    <div className="p-6 max-w-md mx-auto bg-white rounded-xl shadow-md">
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <Label htmlFor="Username">Email</Label>
          <Input
            id="Username"
            type="text"
            value={Username}
            onChange={(e) => setUsername(e.target.value)}
          />
        </div>
        <div>
          <Label htmlFor="Password">Password</Label>
          <Input
            id="Password"
            type="password"
            value={Password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>
        <Button type="submit" disabled={isPending}>
          {isPending ? "Login..." : "Login"}
        </Button>
        <br />
        <Link
          to="/signup"
          className="inline-block mt-2 px-4 py-2 bg-blue-100 text-blue-800 hover:text-pink-700 font-medium rounded-md shadow"
        >
          Signup
        </Link>
      </form>
    </div>
  );
}

export default Login;
