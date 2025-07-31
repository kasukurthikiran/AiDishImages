import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav className="bg-pink-300 p-4 text-center">
      <div className="flex justify-between">
        <Link
          to="/login"
          className="text-blue-800 hover:text-pink-700 font-medium"
        >
          Login
        </Link>
        <Link
          to="/home"
          className="text-blue-800 hover:text-pink-700 font-medium"
        >
          Home
        </Link>
        <Link
          to="/newrestaurant"
          className="text-blue-800 hover:text-pink-700 font-medium"
        >
          New Restaurant
        </Link>
        <Link
          to="/logout"
          className="text-blue-800 hover:text-pink-700 font-medium"
        >
          LogOut
        </Link>
      </div>
    </nav>
  );
}

export default Navbar;
