const Error = () => {
  return (
    <div className="flex flex-col items-center justify-center h-screen gap-4">
      <img
        src="/useImages/error.png"
        alt="Error"
        className="w-48 h-48 object-contain"
      />
      <p className="text-lg font-semibold text-red-600">
        Oops! Something went wrong
      </p>
    </div>
  );
};

export default Error;
