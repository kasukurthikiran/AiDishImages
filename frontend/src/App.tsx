import "./App.css";
import { redirect, Route, Routes } from "react-router-dom";
import Navbar from "./Navbar";
import { Home } from "./components/Home";
import Login from "./components/Login";
import Logout from "./components/Logout";
import SignUp from "./components/SignUp";
import UploadForm from "./components/NewRestaurant";
import { DishImages } from "./components/DishImages";

function App() {
  return (
    <div>
      <Navbar />
      <Routes>
        <Route
          path="/home"
          element={<Home />}
          loader={() => {
            if (localStorage.getItem("token")) {
              return null;
            }
            throw redirect("/login");
          }}
        />
        <Route
          path="/login"
          element={<Login />}
          loader={() => {
            if (localStorage.getItem("token")) {
              throw redirect("/home");
            }
            return null;
          }}
        />
        <Route path="/logout" element={<Logout />} />
        <Route path="/dishes" element={<DishImages />} />
        <Route path="/" element={<UploadForm />} />
        <Route path="/signup" element={<SignUp />} />
      </Routes>
    </div>
  );
}

export default App;
