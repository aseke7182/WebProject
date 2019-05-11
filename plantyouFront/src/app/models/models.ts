export interface Catalog{
    id: number;
    name: string;
    image: string;
}

export interface Food{
    id: number;
    name: string;
    portion: number;
}

export interface Auth{
    token: string;
}
export interface Developer{
    id: number;
    name: string;
    email: string;
    github: string;
    phone: number;
}