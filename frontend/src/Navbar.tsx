import { useEffect, useState } from "react";
import { Link, useNavigate } from "react-router-dom";

function Navbar() {
  const [token, setToken] = useState(localStorage.getItem("token"));
  const navigate = useNavigate();

  useEffect(() => {
    const handleStorageChange = () => {
      setToken(localStorage.getItem("token"));
    };

    window.addEventListener("storage", handleStorageChange);
    return () => {
      window.removeEventListener("storage", handleStorageChange);
    };
  }, []);

  const handleLogout = () => {
    localStorage.removeItem("token");
    window.dispatchEvent(new Event("storage"));
    navigate("/login");
  };

  return (
    <nav className="bg-pink-300 p-4 text-center">
      <div className="flex justify-between">
        {!token && (
          <Link
            to="/login"
            className="text-blue-800 hover:text-pink-700 font-medium"
          >
            Login
          </Link>
        )}

        {token && (
          <>
            <Link
              to="/home"
              className="text-blue-800 hover:text-pink-700 font-medium"
            >
              Home
            </Link>

            <Link
              to="/restaurant"
              className="text-blue-800 hover:text-pink-700 font-medium"
            >
              New Restaurant
            </Link>

            {/* Logout Button */}
            <button
              onClick={handleLogout}
              className="text-blue-800 hover:text-pink-700 font-medium"
            >
              Logout
            </button>
          </>
        )}
      </div>
    </nav>
  );
}

export default Navbar;
