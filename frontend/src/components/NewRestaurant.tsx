"use client";
import { useState } from "react";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Label } from "@/components/ui/label";
import { useRestaurantStore } from "@/store/Store";
import { useNavigate } from "react-router-dom";
import useUploadData from "../customHooks/useUploadData";
import Error from "../customHooks/useError";
export default function UploadForm() {
  const [restaurantName, setRestaurantName] = useState("");
  const [file, setFile] = useState<File | null>(null);
  const restaurant_ids = useRestaurantStore((state) => state.restaurant_ids);
  const setRestaurant_ids = useRestaurantStore(
    (state) => state.setRestaurant_ids
  );
  const navigate = useNavigate();

  const { mutate, data, error, isPending, isSuccess, isError } =
    useUploadData();

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!file || !restaurantName) {
      alert("Please fill all fields.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);
    formData.append("restaurant_name", restaurantName);
    console.log(formData);
    mutate(formData, {
      onSuccess: (data) => {
        setRestaurant_ids(data.restaurant_ids);

        console.log("Upload success:", data);
        console.log("restaurant_ids", restaurant_ids);
        console.log("data.restaurant_ids", data.restaurant_ids);

        const query = data.restaurant_ids;
        navigate(`/poolexample?id=${query}`);
      },
      onError: (error) => {
        <div>
          {<Error />}
          Error loading dishes
        </div>;
        console.error("Upload failed:", error);
      },
    });
  };

  return (
    <div className="p-6 max-w-md mx-auto bg-white rounded-xl shadow-md">
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <Label htmlFor="restaurantName">Restaurant Name</Label>
          <Input
            id="restaurantName"
            type="text"
            value={restaurantName}
            onChange={(e) => setRestaurantName(e.target.value)}
          />
        </div>

        <div>
          <Label htmlFor="file">Upload Image</Label>
          <Input
            id="file"
            type="file"
            accept="image/*"
            onChange={(e) => setFile(e.target.files?.[0] || null)}
          />
        </div>

        <Button
          type="submit"
          disabled={isPending}
          className="flex items-center gap-2"
        >
          {isPending && (
            <svg
              className="animate-spin h-5 w-5 text-white"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
            >
              <circle
                className="opacity-25"
                cx="12"
                cy="12"
                r="10"
                stroke="currentColor"
                strokeWidth="4"
              ></circle>
              <path
                className="opacity-75"
                fill="currentColor"
                d="M4 12a8 8 0 018-8v4l3-3-3-3v4a8 8 0 100 16 8 8 0 01-8-8z"
              ></path>
            </svg>
          )}
          {isPending ? "Uploading..." : "Submit"}
        </Button>
      </form>
    </div>
  );
}
