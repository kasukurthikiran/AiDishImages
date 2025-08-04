import { MoonLoader } from "react-spinners";

function Loading() {
  return (
    <div className="flex justify-center items-center h-screen">
      <MoonLoader color="#36d7b7" size={60} />
    </div>
  );
}

export default Loading;
