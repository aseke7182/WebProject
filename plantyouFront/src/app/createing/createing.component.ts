import { Component, OnInit } from '@angular/core';
import {Ingredient} from '../models/models';
import {ProviderService} from '../services/provider.service';

@Component({
  selector: 'app-createing',
  templateUrl: './createing.component.html',
  styleUrls: ['./createing.component.css']
})
export class CreateingComponent implements OnInit {
  public name = '';
  public  amounts: number;
  constructor(private provider: ProviderService) { }

  ngOnInit() {
  }
  createIngredient(){
    return this.provider.createIngredient(this.name,this.amounts).then(res=>{
      alert("New Ingredient Added Successfully");
    })
  }

}
