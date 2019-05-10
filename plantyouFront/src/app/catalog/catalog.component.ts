import { Component, OnInit } from '@angular/core';
import {Catalog} from '../models/models'
import {ProviderService} from '../services/provider.service';

@Component({
  selector: 'app-catalog',
  templateUrl: './catalog.component.html',
  styleUrls: ['./catalog.component.css']
})
export class CatalogComponent implements OnInit {
  public catalog: Catalog[] = [];

  constructor( private provider: ProviderService ) { }

  ngOnInit() {
    this.getCatalog();
  }

  getCatalog(){
    this.provider.getCatalogList().then(res => {
        this.catalog = res;
    });
  }


}
