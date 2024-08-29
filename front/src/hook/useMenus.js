import {useEffect, useState} from "react";
import axios from "axios";

const defaultImage = "https://media.istockphoto.com/id/497959594/fr/photo/des-g%C3%A2teaux.jpg?s=612x612&w=0&k=20&c=NY1Jnj-x55j4nNzACA-7wIhQuMifw-5Db7GNei09opM="

const useMenus = () => {
    const [menus, setMenus] = useState([]);
    const [desserts, setDesserts] = useState([]);

    useEffect(() => {
        (async () => {
            try {
                const response = await axios.get("http://localhost:8000/api/menu-du-jour/")
                await setMenus(response.data.plats.map(x => ({id: x.id, name: x.nom, price: x.prix, image: x.image_url})));
                await setDesserts(response.data.plats.map(x => ({id: x.id, name: x.nom, price: x.prix, image: defaultImage})));
            }
            catch(e) {
                console.error(e)
            }
        })()
    }, []);

    return {menus, desserts}
}

export default useMenus;