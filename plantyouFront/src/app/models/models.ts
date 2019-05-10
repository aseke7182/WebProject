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