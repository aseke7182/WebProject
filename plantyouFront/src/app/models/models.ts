export interface Catalog{
    id: number;
    name: string;
    image: string;
}

export interface Ingredient{
    id: number;
    name: string;
    amounts: number;
}

export interface Food{
    id: number;
    name: string;
    portion: number;
    price: number;
    ingredients: [];
}

export interface Auth{
    token: string;
    username: string;
}
export interface Developer{
    id: number;
    name: string;
    email: string;
    github: string;
    phone: number;
}

export interface Check{
    id:number;
    status: string;
    cost: number;
    foods: []
}