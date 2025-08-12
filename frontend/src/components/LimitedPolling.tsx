// LimitedPolling.tsx
import { Card, CardHeader } from "@/components/ui/card";
import { useSearchParams } from "react-router-dom";
import { usePolling } from "../customHooks/usePolling";
import type { Dish } from "../customHooks/types";
import { DishCard } from "../customHooks/DishCard";

export default function LimitedPolling() {
  const [searchParams] = useSearchParams();
  const qid = searchParams.get("id") ?? "";
  const token = localStorage.getItem("token");

  const fetchDishes = async (): Promise<{ dishes: Dish[] }> => {
    const response = await fetch(
      `http://localhost:8000/dishes_by_r_id?id=${qid}`,
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
    return await response.json();
  };

  const dishesData = usePolling<{ dishes: Dish[] }>(
    fetchDishes,
    fetchDishes.some((d) => d.image_path === ""),
    1000
  );

  const dishes = dishesData?.dishes ?? [];

  if (!dishes.length) {
    return (
      <Card className="shadow-md col-span-full">
        <CardHeader className="text-center font-bold text-lg text-gray-500">
          No data found
        </CardHeader>
      </Card>
    );
  }

  return (
    <div className="grid grid-cols-1 gap-6 p-4">
      {dishes.map((dish) => (
        <DishCard key={dish.id} dish={dish} />
      ))}
    </div>
  );
}
