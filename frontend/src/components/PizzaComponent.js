const PizzaComponent = ({pizza}) => {
    return (
        <div>
            <div>{JSON.stringify(pizza)}</div>
        </div>
    );
};

export {PizzaComponent};