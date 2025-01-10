import {useForm} from "react-hook-form";
import {pizzaService} from "../services/pizzaService";

const PizzaForm = () => {
    const {register, handleSubmit, reset} = useForm();

    const save = async (pizza) =>{
        await pizzaService.create(pizza)
    }
    return (
        <form onSubmit={handleSubmit(save)}>
            <input type="text" placeholder={'name'} {...register('name')}/>
            <input type="text" placeholder={'size'} {...register('size')}/>
            <input type="text" placeholder={'price'} {...register('price')}/>
            <input type="text" placeholder={'day'} {...register('day')}/>
            <button>save</button>
        </form>
    );
};

export {PizzaForm};