import { Card, CardHeader } from "@/components/ui/card";
import { useEffect, useState } from "react";
import { useSearchParams } from "react-router-dom";

function LimitedLimitedPolling() {
  const [data, setData] = useState<any[]>([]);
  const [searchParams] = useSearchParams();
  const qids = searchParams.get("id");
  const token = localStorage.getItem("token");

  let shouldPoll = data.some((dish) => dish.image_path === "");

  const fetchData = async () => {
    try {
      const response = await fetch(
        `https://menu-api.konic.run/dishes_by_r_id?id=${qids}`,
        {
          method: "GET",
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      const result = await response.json();
      console.log(result);
      setData(() => [...result.dishes]);
      console.log(result.dishes);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  useEffect(() => {
    console.log("i am 1 use effct ");
    fetchData();
  }, []);

  useEffect(() => {
    console.log("i am second useEffect");
    if (!shouldPoll) return;

    const intervalId = setInterval(() => {
      fetchData();
    }, 1000);

    return () => clearInterval(intervalId);
  }, [shouldPoll]);

  return (
    <div className="grid grid-cols-1 md:grid-cols-1 gap-6 p-4">
      {!data || data.length === 0 ? (
        <Card className="shadow-md col-span-full">
          <CardHeader className="text-center font-bold text-lg text-gray-500">
            No data found
          </CardHeader>
        </Card>
      ) : (
        data.map((dish: any) => (
          <div className="max-w-xl mx-auto my-4" key={dish.id}>
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
        ))
      )}
    </div>
  );
}

export default LimitedLimitedPolling;
