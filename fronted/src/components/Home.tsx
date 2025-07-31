("use client");
import useAllDishes from "../my_hooks/UseAllDishes";

import { Card, CardHeader } from "@/components/ui/card";

export const Home = () => {
  const { data, isLoading, error } = useAllDishes();
  console.log("i am data", data);
  if (isLoading) return <div>Loading dishes...</div>;
  if (error) return <div>Error loading dishes</div>;

  return (
    <div className="grid grid-cols-1 md:grid-cols-1 gap-6 p-4">
      {!data || data.dishes.length === 0 ? (
        <Card className="shadow-md col-span-full">
          <CardHeader className="text-center font-bold text-lg text-gray-500">
            No data found
          </CardHeader>
        </Card>
      ) : (
        data.dishes.map((dish: any) => (
          <div className="max-w-xl mx-auto my-4">
            <Card
              key={dish.id}
              className="p-4 shadow-md flex gap-4 items-start"
            >
              <div className="w-90 h-90 flex-shrink-0">
                <img
                  src={dish.signed_url}
                  alt={dish.name}
                  className="w-80 h-75 object-cover rounded-md"
                />
              </div>

              <div className="flex flex-col justify-center">
                <h3 className="text-xl font-bold">{dish.name}</h3>
                <p className="text-gray-600">
                  Restaurant: {dish.restaurant_name}
                </p>
                {/* <p className="text-green-600 font-semibold">
                  Price: ₹{dish.price}
                </p> */}
              </div>
            </Card>
          </div>
        ))
      )}
    </div>
  );
};
