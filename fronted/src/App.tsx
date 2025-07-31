import "./App.css";
import { Route, Routes } from "react-router-dom";
import Navbar from "./Navbar";
import { Home } from "./components/Home";
import Login from "./components/Login";
import Logout from "./components/SignUp";
import UploadForm from "./components/NewRestaurant";
import { DishImages } from "./components/DishImages";

function App() {
  return (
    <div>
      <Navbar />
      <Routes>
        <Route path="/home" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/logout" element={<Logout />} />
        <Route path="/dishes" element={<DishImages />} />
        <Route path="/newrestaurant" element={<UploadForm />} />
      </Routes>
    </div>
  );
}

export default App;
