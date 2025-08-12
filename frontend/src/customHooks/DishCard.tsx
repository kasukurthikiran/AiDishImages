// DishCard.tsx
import { Card, CardHeader } from "@/components/ui/card";
import type { Dish } from "./types";

interface DishCardProps {
  dish: Dish;
}

export function DishCard({ dish }: DishCardProps) {
  return (
    <div className="max-w-xl mx-auto my-4">
      <Card className="p-4 shadow-md flex gap-4 items-start">
        <div className="w-80 h-60 flex-shrink-0">
          <img
            src={dish.signed_url}
            alt={dish.name}
            className="w-full h-full object-cover rounded-md"
          />
        </div>

        <div className="flex flex-col justify-center">
          <h3 className="text-xl font-bold">{dish.name}</h3>
          <p className="text-gray-600">Restaurant: {dish.restaurant_name}</p>
        </div>
      </Card>
    </div>
  );
}
