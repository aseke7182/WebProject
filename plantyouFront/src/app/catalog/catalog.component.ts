import { Component, OnInit } from '@angular/core';
import {Catalog, Food} from '../models/models'
import {ProviderService} from '../services/provider.service';

@Component({
  selector: 'app-catalog',
  templateUrl: './catalog.component.html',
  styleUrls: ['./catalog.component.css']
})
export class CatalogComponent implements OnInit {
  public catalog: Catalog[] = [];
  public food: Food[] = [];
  public foodscatalog: Catalog;
  public IsCatalog = true;
  constructor( private provider: ProviderService ) { }

  ngOnInit() {
    this.getCatalog();
  }

  ChangeStatus(catalog1: Catalog){
    this.foodscatalog= catalog1;
    this.IsCatalog = !this.IsCatalog;
    if(this.IsCatalog==false){
      this.getFood();
    }
  }
  getCatalog(){
    this.provider.getCatalogList().then(res => {
        this.catalog = res;
    });
  }
  getFood(){
    this.provider.getFood(this.foodscatalog).then(res =>{
      this.food = res;
    }).catch(res =>{
      alert("WRONG");
    })
  }


}
