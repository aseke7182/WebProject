import { Injectable } from '@angular/core';
import {Catalog,Food,Auth,Developer,Ingredient,Check} from '../models/models';
import {MainService} from './main.service';
import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService  {

  constructor(http: HttpClient) {
    super(http);
   }

  signup(username: any, email: any, password: any): Promise<Auth>{
    return this.post('http://127.0.0.1:8000/api/signup/',{
      username: username,
      email: email,
      password: password
    })
  }
  login(username: any , password: any): Promise<Auth>{
    return this.post('http://127.0.0.1:8000/api/login/',{
      username: username,
      password: password
    })
  }
  logout(): Promise<any>{
    return this.post('http://127.0.0.1:8000/api/logout/',{})
  }
  getCatalogList(): Promise<Catalog[]>{
    return this.get('http://127.0.0.1:8000/api/catalogs/',{})
  }
  getFood(food: Catalog): Promise<Food[]>{
    return this.get(`http://127.0.0.1:8000/api/catalogs/${food.id}/foods/`,{})
  }
  getDevelopers(): Promise<Developer[]>{
    return this.get('http://127.0.0.1:8000/api/developers/',{});
  }
  userFoodList(catalog: Catalog): Promise<Food[]>{
    return this.get(`http://127.0.0.1:8000/api/userfoods/${catalog.id}`,{})
  }
  deleteFood(catalog: Catalog,food: Food): Promise<any>{
    return this.delet(`http://127.0.0.1:8000/api/catalogs/${catalog.id}/foods/${food.id}/`,{});
  }
  updateFood(catalog: Catalog,food: Food): Promise<Food>{
    return this.put(`http://127.0.0.1:8000/api/catalogs/${catalog.id}/foods/${food.id}/`,{
      name: food.name,
      portion: food.portion,
      catalog: catalog.id,
      price: food.price,
      ingredients: food.ingredients
    });
  }
  createFood(catalog: Catalog,arr:number[], name: string, portion: number, price:number  ): Promise<Food>{
    return this.post(`http://127.0.0.1:8000/api/catalogs/${catalog.id}/foods/`,{
      name: name,
      portion: portion,
      catalog: catalog.id,
      price: price,
      ingr: arr
    })
  }
  getIngredients(): Promise<Ingredient[]>{
    return this.get('http://127.0.0.1:8000/api/ingredients/',{});
  }
  createIngredient(name:string, amounts: number): Promise<Ingredient>{
    return this.post('http://127.0.0.1:8000/api/ingredients/',{
      name: name,
      amounts:amounts
    })
  }
  getChecks(): Promise<Check[]>{
    return this.get('http://127.0.0.1:8000/api/checks/',{});
  }
  createCheck(arr: number[]): Promise<Check>{
    return this.post('http://127.0.0.1:8000/api/checks/',{
      status: "undone",
      fo: arr
    })
  }
}
