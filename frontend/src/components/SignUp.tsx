import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Label } from "@radix-ui/react-label";
import { Input } from "./ui/input";
import { Button } from "./ui/button";
import useSignup from "@/customHooks/useSignUp";

function SignUp() {
  const [Username, setUsername] = useState("");
  const [Email, setEmail] = useState("");
  const [Password, setPassword] = useState("");
  const navigate = useNavigate();

  const { data, mutate, isPending } = useSignup();

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    if (!Username || !Email || !Password) {
      alert("Please fill all fields.");
      return;
    }

    mutate(
      {
        name: Username,
        email: Email,
        password: Password,
      },
      {
        onSuccess: (data) => {
          alert("Registration successful!");
          setUsername("");
          setEmail("");
          setPassword("");
          navigate(`/`);
        },
        onError: (error) => {
          alert("Registration failed: " + error.response?.data?.detail);
          setUsername("");
          setEmail("");
          setPassword("");
        },
      }
    );
  };

  return (
    <div className="p-6 max-w-md mx-auto bg-white rounded-xl shadow-md">
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <Label htmlFor="Username">Username</Label>
          <Input
            id="Username"
            type="text"
            value={Username}
            onChange={(e) => setUsername(e.target.value)}
          />
        </div>

        <div>
          <Label htmlFor="Email">Email</Label>
          <Input
            id="Email"
            type="email"
            value={Email}
            onChange={(e) => setEmail(e.target.value)}
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
          {isPending ? "Registering..." : "Submit"}
        </Button>
      </form>
    </div>
  );
}

export default SignUp;
