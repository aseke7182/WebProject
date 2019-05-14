import { Component, OnInit, Provider } from '@angular/core';
import {Food, Catalog, Ingredient} from '../models/models';
import {ProviderService} from '../services/provider.service';
@Component({
  selector: 'app-createfood',
  templateUrl: './createfood.component.html',
  styleUrls: ['./createfood.component.css']
})
export class CreatefoodComponent implements OnInit {
  public currentCatalog: Catalog;
  public IsCatalog = true;
  public catalog: Catalog[] =[];
  public ing: Ingredient[]=[];
  public arr: number[]=[];
  public name = "";
  public portion: number;
  public price: number;
  constructor(private provider: ProviderService) { }

  ngOnInit() {
    this.getCatalog();
  }
  getCatalog(){
    this.provider.getCatalogList().then(res => {
        this.catalog = res;
    });
  }
  createFood(){
    this.provider.createFood(this.currentCatalog,this.arr,this.name,this.portion,this.price).then(res =>{
      alert("Food Added Successfully");
    })
  }
  ChangeStatus(catalog1: Catalog){
    this.currentCatalog= catalog1;
    this.IsCatalog = !this.IsCatalog;
    this.getIng();
  }
  getIng(){
    this.provider.getIngredients().then(res=>{
      console.log(res);
      this.ing = res;
    })
  }
  addIng(id:number){
    this.arr.push(id);
  }
}
