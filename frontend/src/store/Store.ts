import { create } from "zustand";
interface ImageDetails {
  signed_url?: string;
  image_path?: string;
  id?: number;
  name?: string;
}

interface Restaurant {
  restaurant_id: string;
  name?: string;
}

interface ImageStore {
  image_urls: ImageDetails[];
  setImage_urls: (details: ImageDetails[]) => void;
}

export const useImageStore = create<ImageStore>((set) => ({
  image_urls: [],
  setImage_urls: (urls) => set({ image_urls: urls }),
}));

interface RestaurantStore {
  restaurant_ids: string;
  setRestaurant_ids: (ids: string) => void;
}

export const useRestaurantStore = create<RestaurantStore>((set) => ({
  restaurant_ids: "",
  setRestaurant_ids: (ids) => set({ restaurant_ids: ids }),
}));
