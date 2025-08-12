import "./App.css";
import { redirect, Route, Routes } from "react-router-dom";
import Navbar from "./Navbar";
import { Home } from "./components/Home";
import Login from "./components/Login";
import Logout from "./components/Logout";
import SignUp from "./components/SignUp";
import UploadForm from "./components/NewRestaurant";
import { DishImages } from "./components/DishImages";
import PoolExample from "./components/PoolDishes";
function App() {
  return (
    <div>
      <Navbar />
      <Routes>
        <Route path="/home" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/logout" element={<Logout />} />
        <Route path="/dishes" element={<DishImages />} />
        <Route path="/restaurant" element={<UploadForm />} />
        <Route path="/signup" element={<SignUp />} />
        <Route path="/poolexample" element={<PoolExample />} />
      </Routes>
    </div>
  );
}

export default App;
