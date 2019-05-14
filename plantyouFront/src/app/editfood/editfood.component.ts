import { Component, OnInit, Provider } from '@angular/core';
import {Food,Catalog} from '../models/models';
import {ProviderService} from '../services/provider.service';
@Component({
  selector: 'app-editfood',
  templateUrl: './editfood.component.html',
  styleUrls: ['./editfood.component.css']
})
export class EditfoodComponent implements OnInit {
  public userList: Food[] = [];
  public catalog: Catalog[] = [];
  public foodscatalog: Catalog;
  public IsCatalog = true;
  constructor(private provider: ProviderService ) { }

  ngOnInit() {
    this.getCatalog()
  }
  getCatalog(){
    this.provider.getCatalogList().then(res => {
        this.catalog = res;
    });
  }
  edit(){
    this.provider.userFoodList(this.foodscatalog).then(res =>{
      this.userList = res;
    })
  }
  ChangeStatus(catalog1: Catalog){
    this.foodscatalog= catalog1;
    this.IsCatalog = !this.IsCatalog;
    if(this.IsCatalog==false){
      this.edit();
    }
  }
  deleteFood(food: Food){
    this.provider.deleteFood(this.foodscatalog,food).then(res=>{
      this.edit();
    })
  }
  saveFood(food: Food){
    this.provider.updateFood(this.foodscatalog,food).then(res=>{
      this.edit()
    })
  }
}
