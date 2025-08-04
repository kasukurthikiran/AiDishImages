import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

function Navbar() {
  const [token, setToken] = useState(localStorage.getItem("token"));

  useEffect(() => {
    const handleStorageChange = () => {
      setToken(localStorage.getItem("token"));
    };

    window.addEventListener("storage", handleStorageChange);

    return () => {
      window.removeEventListener("storage", handleStorageChange);
    };
  }, [token]);

  return (
    <nav className="bg-pink-300 p-4 text-center">
      <div className="flex justify-between">
        {!token ? (
          <Link
            to="/login"
            className="text-blue-800 hover:text-pink-700 font-medium"
          >
            Login
          </Link>
        ) : null}
        {token ? (
          <Link
            to="/home"
            className="text-blue-800 hover:text-pink-700 font-medium"
          >
            Home
          </Link>
        ) : null}

        {token ? (
          <Link to="" className="text-blue-800 hover:text-pink-700 font-medium">
            New Restaurant
          </Link>
        ) : null}

        <Link
          to="/logout"
          className="text-blue-800 hover:text-pink-700 font-medium"
        >
          Logout
        </Link>
      </div>
    </nav>
  );
}

export default Navbar;
