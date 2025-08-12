"use client";

import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import Loading from "@/customHooks/useLoading";
import Error from "@/customHooks/useError";
import UseAllRestaurant from "@/customHooks/useRestaurant";
import {
  Carousel,
  CarouselContent,
  CarouselItem,
  CarouselNext,
  CarouselPrevious,
} from "@/components/ui/carousel";
import { type CarouselApi } from "@/components/ui/carousel";

export const Home = () => {
  const { data, isLoading, error, isError } = UseAllRestaurant();
  const navigate = useNavigate();

  const [api, setApi] = useState<CarouselApi | undefined>(undefined);
  const [current, setCurrent] = useState(0);
  const [count, setCount] = useState(0);

  useEffect(() => {
    if (!api) return;

    setCount(api.scrollSnapList().length);
    setCurrent(api.selectedScrollSnap() + 1);

    const handleSelect = () => {
      setCurrent(api.selectedScrollSnap() + 1);
    };

    api.on("select", handleSelect);
    return () => {
      api.off("select", handleSelect);
    };
  }, [api]);

  if (isLoading) {
    return (
      <div className="flex flex-col items-center justify-center h-screen gap-4">
        <p className="font-bold text-lg text-gray-600 animate-pulse">
          Loading restaurants...
        </p>
        <Loading />
      </div>
    );
  }

  if (isError) {
    return (
      <div className="flex flex-col items-center justify-center h-screen gap-4">
        <p className="font-bold text-lg text-gray-600">
          Error loading restaurants
        </p>
        <Error />
      </div>
    );
  }

  return (
    <div className="p-4">
      <Carousel setApi={setApi} className="relative">
        <CarouselContent>
          {data?.restaurants_data?.map(
            (restaurant: { id: string; name: string }) => (
              <CarouselItem key={restaurant.id} className="basis-1/1 p-4">
                <div
                  className="bg-white shadow-md rounded-lg p-6 text-center cursor-pointer hover:shadow-lg transition h-48 flex items-center justify-center"
                  onClick={() => navigate(`/dishes?id=${restaurant.id}`)}
                >
                  <h2 className="font-bold text-lg text-amber-700">
                    {restaurant.name}
                  </h2>
                </div>
              </CarouselItem>
            )
          )}
        </CarouselContent>

        <CarouselPrevious className="absolute left-2 top-1/2 -translate-y-1/2" />
        <CarouselNext className="absolute right-2 top-1/2 -translate-y-1/2" />
      </Carousel>

      <p className="text-center mt-4 text-gray-600">
        Slide {current} of {count}
      </p>
    </div>
  );
};
