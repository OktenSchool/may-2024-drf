import {PizzaForm} from "../components/PizzaForm";
import {PizzasComponent} from "../components/PizzasComponent";
import {Chat} from "../components/Chat";

const PizzasPage = () => {
    return (
        <div>
            <PizzaForm/>
            <hr/>
            <PizzasComponent/>
            <hr/>
            <Chat/>
        </div>
    );
};

export {PizzasPage};