import {useState} from "react";


const useMyMenus = () => {
    const [myMenus, setMyMenus] = useState([]);

    const addPlat = (menu) => {
        const isItem = myMenus.find(x => menu.id === x.id)
        if (isItem)
            window.alert("Vous avez déja cette plat dans votre panier")
        else
            setMyMenus([...myMenus, menu]);
    }

    const removePlat = (removedMenu) => {
        setMyMenus(myMenus.filter(menu => removedMenu.id !== menu.id))
    }

    return {myMenus, addPlat, removePlat}
}

export default useMyMenus;