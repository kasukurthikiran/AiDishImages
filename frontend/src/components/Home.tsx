"use client";
import Loading from "@/customHooks/useLoading";
import useAllDishes from "../customHooks/UseAllDishes";
import Error from "@/customHooks/useError";
import { Card, CardHeader } from "@/components/ui/card";
import * as React from "react";
import { CheckIcon, ChevronsUpDownIcon } from "lucide-react";
import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";
import {
  Command,
  CommandEmpty,
  CommandGroup,
  CommandInput,
  CommandItem,
  CommandList,
} from "@/components/ui/command";
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover";

export const Home = () => {
  const { data, isLoading, error } = useAllDishes();
  const [open, setOpen] = React.useState(false);
  const [restaurant_id, setRestaurant_id] = React.useState("");
  const [tempRestaurantId, setTempRestaurantId] = React.useState("");

  if (isLoading) {
    return (
      <div className="flex flex-col items-center justify-center h-screen gap-4">
        <p className="font-bold text-lg text-gray-600 animate-pulse">
          Loading dishes...
        </p>
        <Loading />
      </div>
    );
  }

  if (error) {
    return (
      <div>
        <p className="font-bold text-lg text-gray-600">Error loading dishes</p>
        <Error />
      </div>
    );
  }

  const uniqueRestaurants = Array.from(
    new Map(
      data?.dishes.map((dish: any) => [
        String(dish.restaurant_id),
        {
          restaurant_id: String(dish.restaurant_id),
          restaurant_name: dish.restaurant_name,
        },
      ])
    ).values()
  );

  return (
    <div className="grid grid-cols-1 gap-6 p-4">
      {!data || data.dishes.length === 0 ? (
        <Card className="shadow-md col-span-full">
          <CardHeader className="text-center font-bold text-lg text-gray-500">
            No data found
          </CardHeader>
        </Card>
      ) : (
        <>
          <div className="flex justify-end mb-4">
            <div className="w-[220px] font-bold text-xl">
              <Popover open={open} onOpenChange={setOpen}>
                <PopoverTrigger asChild>
                  <Button
                    variant="outline"
                    role="combobox"
                    aria-expanded={open}
                    className="w-[220px] justify-between"
                  >
                    {restaurant_id
                      ? uniqueRestaurants.find(
                          (rest) => rest.restaurant_id === restaurant_id
                        )?.restaurant_name
                      : "Select Restaurant..."}
                    <ChevronsUpDownIcon className="ml-2 h-4 w-4 shrink-0 opacity-50" />
                  </Button>
                </PopoverTrigger>

                <PopoverContent className="w-[250px] p-0">
                  <Command>
                    <CommandInput placeholder="Search restaurant..." />
                    <CommandList>
                      <CommandEmpty>No Restaurant found.</CommandEmpty>
                      <CommandGroup>
                        {uniqueRestaurants.map((restaurant: any) => (
                          <CommandItem
                            key={restaurant.restaurant_id}
                            value={restaurant.restaurant_id}
                            onSelect={(currentValue) => {
                              setTempRestaurantId(currentValue);
                            }}
                          >
                            <CheckIcon
                              className={cn(
                                "mr-2 h-4 w-4",
                                tempRestaurantId === restaurant.restaurant_id
                                  ? "opacity-100"
                                  : "opacity-0"
                              )}
                            />
                            {restaurant.restaurant_name}
                          </CommandItem>
                        ))}
                      </CommandGroup>
                    </CommandList>

                    <div className="flex justify-between gap-2 p-2 border-t">
                      <Button
                        size="sm"
                        variant="outline"
                        onClick={() => {
                          setTempRestaurantId("");
                          setOpen(false);
                        }}
                      >
                        Cancel
                      </Button>
                      <Button
                        size="sm"
                        onClick={() => {
                          setRestaurant_id(tempRestaurantId);
                          setOpen(false);
                        }}
                        disabled={!tempRestaurantId}
                      >
                        Submit
                      </Button>
                    </div>
                  </Command>
                </PopoverContent>
              </Popover>
            </div>
          </div>

          {data.dishes
            .filter((dish: any) =>
              restaurant_id
                ? String(dish.restaurant_id) === restaurant_id
                : true
            )
            .map((dish: any) => (
              <div key={dish.id} className="max-w-xl mx-auto my-4">
                <Card className="p-4 shadow-md flex gap-4 items-start">
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
                  </div>
                </Card>
              </div>
            ))}
        </>
      )}
    </div>
  );
};
